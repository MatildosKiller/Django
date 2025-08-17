from django.db import models
from django.db.models import F
import asyncio
# Create your models here.
from django.db import connection
 
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()



async def acreate_person(name_arg, age_arg):
    person = await Person.objects.acreate(name=name_arg, age=age_arg)
    print(person.name)

async def abulc_create_persons():
    people = Person.objects.bulk_create([Person(name="Kate", age=24),Person(name="Ann", age=21),])
    


async def update_or_create_person():
    values_for_update={"name":"Bob", "age": 31}
    bob, created = Person.objects.aupdate_or_create(id=2, defaults = values_for_update)
    if(created):print("создан новый объект")

async def update_person(_id):
    Person.objects.filter(id=_id).aupdate(age = F("age") + 1) 


async def bulk_update_person():
    first_person = Person.objects.get(id=1)
    first_person.name = "Tomas"
    second_person = Person.objects.get(id=2)
    second_person.age = 29
    number = Person.objects.abulk_update([first_person, second_person], ["name", "age"])
    print(number)

async def delete_person(_id):
   pers = Person.objects.get(id=_id)
   pers.adelete() 

async def delete_person_querry(_id):
   Person.objects.filter(id=_id).delete()

def make_querry():
    # определяем значение для параметра name
    name_for_filter = "Tom"
# определяем значение для параметра age
    age_for_filter = 35
 
    people = Person.objects.raw("SELECT * FROM hello_person WHERE name = %s OR age > %s",
                                [name_for_filter, age_for_filter])
    
    with connection.cursor() as cursor:
        cursor.execute("UPDATE hello_person SET name ='Tomas' WHERE name='Tom' AND age=31")
        cursor.execute("SELECT * FROM hello_person WHERE name = 'Tomas'")
        row = cursor.fetchone()     # получаем одну строку
        print(row)
    # people = Person.objects.raw("SELECT id, name FROM hello_person")


make_querry()