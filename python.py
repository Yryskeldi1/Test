############1
import math
class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
   
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

# kgtopounds = KgToPounds(23)
# print(kgtopounds.to_pounds())
# print(kgtopounds.kg)
# kgtopounds.kg = 19
# print(kgtopounds.kg)
# kgtopounds.kg = 'один'


########2
class Mathh:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __sub__(self):
        return self.a - self.b

    def __add__(self):
         return self.a + self.b
         
# mathh = Mathh(15, 10)
# print(mathh.__sub__())
# print(mathh.__add__())


########3
class Soda:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')

# gazz1 = Soda('арбуз')
# gazz2 = Soda(5)
# gazz1.show_my_drink()
# gazz2.show_my_drink()


#########4
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name_surname(self):
        return self.name + ' ' + self.surname

    @name_surname.setter
    def name_surname(self, new):
        self.name, self.surname = new.split(' ')

# person = Person('Yrys', 'Ysmailov')
# print(person.name_surname)
# person.name_surname = 'Akbar Abarov'
# print(person.name_surname)


######5
import random
class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Doberman', 'Alabai', 'layka', 'Beagle'])

    def fetch(self, thing):
        print('% goes after the %s!' %(self.name, thing))

d = Dog('dogname')
# print(d.name)
# print(d.breed)