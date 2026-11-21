#1.Car class with display_info method to show brand, model, and year of the car.

class Car:
    def  __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}.")
        
car1 = Car("Toyota","Camry",2020)
car2 = Car("Honda","Civic",2019)
car3 = Car("Ford","Mustang",2021)

car1.display_info()
car2.display_info()
car3.display_info()

#2.Counter class with class Attribute & @classmethod to keep track of the number of instances created.

class Counter:
    total_objects = 0
    
    def __init__(self):
        Counter.total_objects += 1
        
    @classmethod
    def get_total_objects(cls):
        return cls.total_objects    
    
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()

print("Total Counter objects created:", Counter.get_total_objects())


#3.circle class with @property for area and circumference.

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    @property
    def area(self):
        return round(math.pi * (self.radius ** 2), 2)
    
    @property
    def circumference(self):
        return round(2 * math.pi * self.radius, 2)
    
circle = Circle(5)
print("Area:", circle.area)
print("Circumference:", circle.circumference)

#4.Employee class with private salary and Getter / setter methods.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,new_salary):
        if new_salary >self.__salary:
            self.__salary = new_salary
            print(f"Salary updated for {self.__salary}.")

        else:
            print("Invalid update:New salary must be higher than current salary.")
        
emp=Employee("John",50000)
print("Initial salary:",emp.get_salary())

emp.set_salary(35000)  # valid increase
emp.set_salary(28000) #invalid decrease
print("Final salary:",emp.get_salary())

#5.Temperature class with celsius setter valodation & REad-only kelvin.

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self,value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        self._celsius = value
        
    @property
    def kelvin(self):
        return round(self._celsius + 273.15, 2)
    
temp = Temperature(25)
print("Celsius:", temp.celsius)
print("Kelvin:", temp.kelvin)

try:
    temp.celsius = -300  # This should raise an error
except ValueError as e:
    print("Error:", e)
    
#6.Rectangle class with __eq__ comparing Area.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False
    
rect1 = Rectangle(4, 6)
rect2 = Rectangle(3, 8)
rect3 = Rectangle(5, 5)

print("rect1 == rect2:", rect1 == rect2) 
print("rect1 == rect3:", rect1 == rect3)

#7.Library class with private __books list.

class Library:
    def __init__(self):
        self.__books = []
        
    def add_book(self, title):
        self.__books.append(title)
        print(f"Added book: {title}")
        
    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(f"Removed book: {title}")
        else:
            print(f"Book not found: {title}")
            
    def list_books(self):
        if not self.__books:
            print("No books in the library.")
        else:
            print("Books in the library:", ",".join(self.__books))
lib = Library()
lib.add_book("Atomic Habits")
lib.add_book("Clean Code")
lib.list_books()
lib.remove_book("Atomic Habits")
lib.list_books()