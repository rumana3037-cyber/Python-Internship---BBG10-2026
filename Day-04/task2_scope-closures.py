#1.Write a function that uses a global variable to keep track of how many times it has
# been called in total, across multiple calls. Call it 4 times and print the final count.

call_count = 0

def track_calls():
    global call_count
    call_count += 1
    
track_calls()
track_calls()
track_calls()
track_calls()

print("Number of times track_calls() was called:", call_count)

#2.Write a closure function make_greeting(language) that returns a function which greets a  name in either English or Hindi depending on the language passed when make_greeting
# was first called. For example, make_greeting("hindi")should return a function  that prints Namaste, <name> when called with a name.

def make_greeting(language):
    def greeting(name):
        if language.lower() == "hindi":
            return f"Namaste, {name}"
        else:
            return f"Hello, {name}"
    return greeting

hindi_greet = make_greeting("hindi")
english_greet = make_greeting("english")

print(hindi_greet("Alice"))
print(english_greet("Bob")) 

#3.Create two completely independent counters using the same closure function from the example, and prove they do not affect each other by calling each one a different number of times and printing both results.

def make_counter(start):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter_a = make_counter(0)
counter_b = make_counter(100)

#call counter_a 3 times
counter_a()
counter_a()
result_a = counter_a()

#call counter_b 2 times
counter_b()
result_b = counter_b()

print("Result for counter_a:", result_a)
print("Result for counter_b:", result_b)

#4.Write a function with a nested inner function where the outer function has a variable status = "pending".
# The inner function should change this to "completed" using nonlocal,and the outer function should print the final status after calling the inner function.

def process_task():
    status = "pending"
    
    def complete_task():
        nonlocal status
        status = "completed"
    
    complete_task()
    print("Final status:", status)
    
process_task()

#5.Write a small script with three variables all named mode, one global, one inside an outer function, and one inside an inner function nested inside that outer function. Print all three at the correct points in the code to clearly show the LEGB lookup order in action.

mode = "global mode"

def outer_function():
    mode = "Enclosing mode"
    
    def inner_function():
        mode = "Local mode"
        print("Inside inner_function:", mode)
        
    inner_function()
    print("Inside outer_function:", mode)
    
outer_function()
print("In global scope:", mode)

#6.Write a closure based function make_validator(min_value) that returns a function which checks if a given number is greater than or equal to min_value.
# Create two different validators with different minimum values and test both with a few numbers.

def make_validator(min_value):
    def validator(num):
        return num >= min_value
    return validator

adult_validator = make_validator(18)
passing_validator = make_validator(40)

print("Age 20 vlid:", adult_validator(20))  # True
print("Age 15 valid:", adult_validator(15))  # False

print("Score 40 valid:", passing_validator(40))  # True
print("Score 35 valid:", passing_validator(35))  # False