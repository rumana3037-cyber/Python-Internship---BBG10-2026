#1.person and student (single inheritance with super()).

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        
    def study(self):
        print(f"{self.name} is studying {self.course}.")    
        
#Test  
student = student("Rumana", 19, "BCA")  
student.study()  

#2.Employee Developer , and Designer (Method Overriding + super() ).

class Employee:
    def calculate_salary(self):
        return 30000

class Developer(Employee):
    def calculate_salary(self):
        base = super().calculate_salary()
        return base + 10000  # Developer bonus

class Designer(Employee):
    def calculate_salary(self):
        base = super().calculate_salary()
        return base + 7000   # Designer bonus

# Test
dev = Developer()
des = Designer()
print("Developer Salary:", dev.calculate_salary())
print("Designer Salary:", des.calculate_salary())
    
    
#3. Account, SavingsAccount , and FixedDeposit (Polymorphism in a loop).

class Account:
    def get_interest_rate(self):
        return 4
    
class SavingsAccount(Account):
    def get_interest_rate(self):
        return 6
    
class FixedDeposit(Account):
    def get_interest_rate(self):
        return 7.5
    
# Test
accounts = [Account(), SavingsAccount(), FixedDeposit()]

for acc in accounts:
    print(f"Interest Rate: {acc.get_interest_rate()}")
    

#4. Bird , Airplane , and Drone (Duck Typing).

class Bird:
    def fly(self):
        print("Bird flaps its wings and flies in the sky.")

class Airplane:
    def fly(self):
        print("Airplane uses jet engines to fly at high altitude.")

class Drone:
    def fly(self):
        print("Drone spins four propellers and hovers in the air.")

def start_flight(flying_object):
    flying_object.fly()

# Test
start_flight(Bird())
start_flight(Airplane())
start_flight(Drone())

#5. Vehicle -> Car -> SportsCar (Multilevel Inheritance).

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Top Speed: {self.top_speed} km/h")

# Test
sc = SportsCar("Porsche", "911", 310)
sc.display_info()

#6. Notification , EmalNotification, and SMSNotifications (Ploymorphic Dispatch).

class Notification:
    def send(self):
        print("Sending a generic notification.")

class EmailNotification(Notification):
    def send(self):
        print("Sending an Email notification to your inbox.")

class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification to your phone.")

# Test
notifications = [
    Notification(),
    EmailNotification(),
    SMSNotification()
]

for note in notifications:
    note.send()