from django.db import models
import asyncio
# Create your models here.

 
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


async def acreate_person():
    person = await Person.objects.acreate(name="Tim", age=26)
    print(person.name)