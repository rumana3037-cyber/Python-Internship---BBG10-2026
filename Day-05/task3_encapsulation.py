#1. Wallet (Private Balance + @Property).
class Wallet:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

# Test
w = Wallet(500)
w.deposit(200)
w.withdraw(150)
print("Current Balance:", w.balance)

#2.Fraction (__add__ and __str__).

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Test
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print("Sum:", f1 + f2)

#3. Inventory (__len__ and __getitem__).

class Inventory:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

# Test
inv = Inventory(["Laptop", "Mouse", "Keyboard"])
print("Total items:", len(inv))
print("First item:", inv[0])

#4. Point (__eq__ and __str__).

class Inventory:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

# Test
inv = Inventory(["Laptop", "Mouse", "Keyboard"])
print("Total items:", len(inv))
print("First item:", inv[0])

#5. Stack (Private List + Push ,Pop , __str__).

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Test
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)
print("Point 1:", p1)
print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)

#5. Stack (Private List + push , pop, __str__).

class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError("Cannot pop from an empty stack.")
        return self.__items.pop()

    def __str__(self):
        return f"Stack (top -> bottom): {self.__items[::-1]}"

# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print("After pop:", s)

#6. Money (__lt__ and __gt__ with Currency Check ).

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare {self.currency} with {other.currency}")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare {self.currency} with {other.currency}")
        return self.amount > other.amount

# Test
m1 = Money(500, "INR")
m2 = Money(800, "INR")
print("m1 < m2:", m1 < m2)
print("m2 > m1:", m2 > m1)

#7. Timer context Manager (__enter__ and __exit__).

import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        elapsed = self.end - self.start
        print(f"Elapsed time: {elapsed:.6f} seconds")

# Test
with Timer():
    total = 0
    for i in range(1_000_000):
        total += i