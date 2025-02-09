from django.shortcuts import render

from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest

 

class Person:
  
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # # return obj.__dict__
        return super().default(obj)


persons=[Person("Bob",27),Person("Joe",78),Person("Mike",16)]

def index(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": address}
   
    return render(request, "index.html", context=data) # context = {"person": Person("Tom")}

# def index(request, id):
    
   
#     if id in range(0, len(persons)):
#         return JsonResponse(persons[id], safe=False, encoder=PersonEncoder)
#     # если нет, то возвращаем ошибку 404
#     else:
#         return HttpResponseNotFound("Not Found!!!!!!!!!!!!!")

def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    
    # если возраст больше 17, то доступ разрешен
    if(age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")    
 
def products(request):
    return HttpResponse("Список товаров")
 
def new(request):
    return HttpResponse("Новые товары")
 
def top(request):
    return HttpResponse("Наиболее популярные товары")

def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    response.set_cookie("dog", "Bobby")
    return response

# получение куки
def get(request,key):
    # получаем куки с ключом username
    value = request.COOKIES[key]
    return HttpResponse(f"Hello {value}")