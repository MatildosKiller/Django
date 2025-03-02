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


def about(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    
    return render(request, "about.html", context=data)



def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

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