"""
URL configuration for metanit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from hello import views
from django.views.generic import TemplateView

# product_patterns = [
#     path("", views.products),
#     path("new", views.new),
#     path("top", views.top),
#     path("comments", views.comments),
#     path("questions", views.questions),
# ]
 
urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]

# urlpatterns = 
#   re_path(r'^about/contact/', views.contact),
#     path('about', views.about, kwargs={"name":"Tom", "age": 38}),
#     path('index', views.index),
#      path("user/<name>", views.user),
#     path("user/<name>/<int:age>",views.user),

# ]
