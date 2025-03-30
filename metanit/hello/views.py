from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

# def index(request):
#     host = request.META["HTTP_HOST"] # получаем адрес сервера
#     user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные браузера
#     path = request.path     # получаем запрошенный путь
     
#     return HttpResponse(f"""
#         <p>Host: {host}</p>
#         <p>Path: {path}</p>
#         <p>User-agent: {user_agent}</p>
#     """, headers={"SecretCode": "21234567"}, status=400, reason = "incorrect!!!!")
 
def index(request):
    header = "Данные пользователя!!!"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
  
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)

def login(request):
    return render(request, "login.html")

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")


def about(request):
    return render(request, "about.html", context={"site":"METANIT"})

def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")
 
def products(request, id):
    return HttpResponse(f"Товар {id}")

 
def new(request):
    return HttpResponse("Новые товары")
 
def top(request):
    return HttpResponse("Наиболее популярные товары")

def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")
 
def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

def temp_index(request):
    return render(request, "temp_index.html")
 