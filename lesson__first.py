# Python File Handling

# f = open('data.txt', 'r')
#
# res = [i for i in f]
# print(res)



# OOP

# class Shakl:
#     a = 9
#     b = 8
#
#     def multiple(self):
#         return  self.a * self.b
#
#     def mult(self, a, b):
#         return a * b
#
# shape = Shakl()



# class Author:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
# class Book:
#     def __init__(self, name, author, price):
#         self.name = name
#         self.author = author
#         self.price = price
#
# abdulla_qodiriy = Author('Abdulla', 'Qodiriy', 56)
# utgan_kunlar = Book('O\'tgan Kunlar', abdulla_qodiriy, 4000000)
#
# print(utgan_kunlar.author.name, utgan_kunlar.author.last_name)




# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# miles = Dog("Miles", 4)
# buddy = Dog("Buddy", 9)
#
# print(miles.species)





class Subject:
    def __init__(self, name, price, during):
        self.name = name
        self.price = price
        self.during = during


class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
class Teacher(Person):
    def __init__(self, name, last_name, age, job, work_addres, subject):
        super().__init__(name, last_name, age)
        self.work_addres = work_addres
        self.subject = []

class Student(Person):
    def __init__(self,name,last_name,age,work_addres):
        super().__init__(name, last_name, age)
        self.work_addres = work_addres


math = Subject('Math', 850000, 8)
student1 = Student('Lusi', 'Zhao', '25', 'Chine')
# print(student1.name, student1.last_name)

