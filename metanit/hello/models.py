from django.db import models
import asyncio
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

people = Person.objects.bulk_create([
    Person(name="Kate", age=24),
    Person(name="Ann", age=21),
])

people_by_age1 = Person.objects.filter(age=32)
for person in people_by_age1:
    print(f"{person.name} - {person.age}")

#     # получаем пользователей, у которых имя равно NULL
# people_by_name = Person.objects.filter(name__exact=None)

#получаем всех пользователей с заданным параметром, игнорируя регистр символов
# tom = Person.objects.get(name__iexact="tom")

people1 = Person.objects.filter(name__contains="o")

people3 = Person.objects.filter(age__in=[32, 35, 38])
# получаем пользователей, у которых возраст меньше или равен 32 
people7 = Person.objects.filter(age__lte=32)
# получаем пользователей, у которых имя начинается с To или to
people8 = Person.objects.filter(name__istartswith="To")


 
# получаем пользователей, у которых возраст установлен
people78 = Person.objects.filter(age__isnull=False)

# получаем пользователей, у которых имя заканчивается на am или om
people9 = Person.objects.filter(name__regex=r"(am|om)$")

async def acreate_person():
    person = await Person.objects.acreate(name="Tim", age=26)
    print(person.name)

people10 = Person.objects.order_by("name")
people11 = Person.objects.order_by("name", "age")
# упорядочиваем по имени по убыванию
people12 = Person.objects.order_by("-name")

people13 = Person.objects.values_list("name", flat=True).distinct()
print(people13)
 
# Результат
# <QuerySet ['Bob', 'Tom', 'Sam', 'Alice', 'Tom']>
# print("результат value_list упрощенный")
# for person in people13:
#     print(person)