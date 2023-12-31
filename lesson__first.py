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
# print(miles.species)





# class Subject:
#     def __init__(self, name, price, during):
#         self.name = name
#         self.price = price
#         self.during = during
#
#
# class Person:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
# class Teacher(Person):
#     def __init__(self, name, last_name, age, job, work_addres, subject):
#         super().__init__(name, last_name, age)
#         self.work_addres = work_addres
#         self.job = job
#         self.subjects = []
#         self.subject = subject
#     def info(self):
#         for i in self.subject:
#             self.subjects.append(i.name)
#         return (f'name: {self.name}, last_name: {self.last_name}, age: {self.age},'
#                 f' job: {self.job}, work_addres: {self.work_addres}, subjects:{self.subjects}')
#
# class Student(Person):
#     def __init__(self,name,last_name,age,work_addres):
#         super().__init__(name, last_name, age)
#         self.work_addres = work_addres
#
#
# math = Subject('Math', 850000, 8)
# music = Subject('Music', 850000, 7)
# student1 = Student('Lusi', 'Zhao', '25', 'Chine')
# teacher1 = Teacher('Sam', 'Smith', '40', 'singing', 'New York', [music])
# print(teacher1.info())
# print(teacher1.name)



# d = [1,2,3,4,5,6]
# print(len(d)) # 6

# a = [1, 6, 45, 5, 3]
# trg = 9
# d = {}
# for i in range(len(a)):
#     # print(i)
#     if trg - a[i] in d:
#         print([ d[trg - a[i]], i ])
#     else:
#         d[a[i]] = i


# class Card_id:
#     def __init__(self, name, card_name, card_id):
#         self.name = name
#         self.card_name = card_name
#         self.__card_id = card_id
#
# cn = Card_id('Bob', 'anorbank', '1623')
# cn1 = Card_id('Jane', 'xalq banki', 'd9i1')
#
# cn.name = 'Tom'
# print(cn.name)
#
# print(cn.__card_id)
# cn.__card_id = '3434'
# print(cn.__card_id)
#
# cn.last_name = 'Brown'
# print(cn.last_name)



# class Year_of_phone:
#     def __init__(self, phone_name, phone_year):
#         self.phone_name = phone_name
#         self.__phone_year = phone_year
#
#     @property
#     def phone_year(self):
#         return self.__phone_year
#
#     @phone_year.setter
#     def phone_year(self, value):
#         if isinstance(value, int):
#             self.__phone_year = value




# class Fruit:
#     def __init__(self, name: str):
#         self._name = name
#
#     def fruit_get(self):
#         print('getter')
#         return self._name
#
#     def fruit_set(self, new_fruit: str):
#         self._name = new_fruit
#
#
# if __name__ == '__main__':
#     fruit = Fruit('Banana')
#     fruit.fruit_set('Kivi')
#     print(fruit.fruit_get())



# class Fruit:
#     def __init__(self, name: str):
#         self._name = name
#
#     @property
#     def fruit_get(self):
#         print('getter')
#         return self._name
#
#     @fruit_get.setter
#     def fruit_get(self, new_fruit):
#         print('setter')
#         self._name = new_fruit
#
#
# if __name__ == '__main__':
#     fruit = Fruit('Banana')
#
#     print(fruit.fruit_get)
#     fruit.fruit_get = 'Kivi'
#     print(fruit.fruit_get)



#
# class Person:
#
#     __slots__ = ('name', 'age')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('John', 50)
# p2 = Person('Bob', 65)
#
# print(p1.name, p1.age)
# print(p2.name, p2.age)
#
# # p1.f_name = 'Brown'
# # p2.f_name = 'Anderson'
#
# # print(p1.f_name)



import enum

# class Months(enum.Enum):
#     january = 1
#     fabuary = 2
#     march = 3
#     april = 4
#     may = 5
#     june = 6
#     july = 7
#     august = 8
#     september = 9
#     october = 10
#     november = 11
#     december = 12


# print(Months['june'].value)
# print(Months.june.name)



class Lang(enum.Enum):
    lang = {
        'en': {
        'Surxondaryo':'Surkhandarya',
        'Qashqadaryo': 'Kashkadarya'
        },
        'ru': {
            'Surxondaryo': 'Сурхандарьинская',
            'Qashqadaryo': 'Кашкадарья'
        }
    }





#
# class Counry(enum.Enum):
#     country = {
#         1: 'Qashqadaryo',
#         2: 'Samarqand',
#         3: 'Buxoro',
#         4: 'Namangan',
#         5: 'Andijon',
#         6: 'Farg\'ona',
#         7: 'Toshkent',
#         8: 'Surxondaryo'
#     }
#
# num = int(input('raqam kiriting: '))
# language = input('tilni tanlang(en, ru, uz): ')
#
# c = Counry.country.value
# l = Lang.lang.value
#
# # print(l['en'].items())
#
#
# def foo():
#     for i, j in c.items():
#         for u in range(i+1):
#             if num == u:
#                 return j
#
# print(foo())






# name = input('fan nomini kiriting: ')
#
# with open('data.txt') as f:
#     o = 1
#     for i in f:
#         if name == i.strip():
#             with open('new_file.txt', 'w') as r:
#                 r.write(f'{name} {o}')
#                 break
#         o += 1







