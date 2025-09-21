from django.db import models
import asyncio
# Create your models here.





class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Company(models.Model):
    name = models.CharField(max_length=30)
 
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()



apple = Company.objects.get(id=1)


apple.product_set.create(name="iPhone 8", price=67890)
