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
from django.urls import path, include
from hello import views
 
product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]
  # path("index/<int:id>", views.index),
urlpatterns = [
    path("", views.index),
    path("access/<int:age>", views.access),
    path("products/", include(product_patterns)),
    path("set", views.set),
    path("get/<str:key>", views.get),
]
