"""This is an example of Python functions"""

import random
from functools import partial

def hello_world():
    """This is a function that prints hello world"""
    print("Hello World")

# Call the function
hello_world()

# An add function
def add(x, y):
    """This is a function that adds two numbers"""
    return x + y

# call the function
print(add(1, 2))


# A function that contains another function
def add_and_multiply(x, y, z): # x, y, z are parameters
    """This is a function that adds two numbers and multiplies them by another number"""
    
    return add(x, y) * z

# call the function
print(add_and_multiply(1, 2, 3))


#### Advanced functions ####
# A function that returns a function
def create_adder(x):
    """This is a function that returns a function that adds x to the input"""
    def adder(y):
        """This is a function that adds x to the input"""
        return x + y
    return adder
# create logging decorator
def logging_decorator(func):
    """This is a function that logs the input and output of a function"""
    def wrapper(*args, **kwargs):
        """This is a function that logs the input and output of a function"""
        print("Input:", args, kwargs)
        result = func(*args, **kwargs)
        print("Output:", result)
        return result
    return wrapper

# use the decorator
@logging_decorator
def add(x, y):
    """This is a function that adds two numbers"""
    return x + y

add(1, 2)

# create a function that returns a generator that is random infinite values between 0 and 1
def random_generator():
    """This is a function that returns a generator that is random infinite values between 0 and 1"""
    while True:
        yield random.random()

#use the function to generate random values and break when we get a value > 0.5
for i in random_generator():
    print(f"My random number is {i}")
    if i > 0.5:
        break
    print(i)

# build a partial fuction that accepts three parameters and multiplies them by each other
def multiply(x, y, z):
    """This is a function that multiplies three numbers"""
    return x * y * z

#call the function with a partial function
print("this won't fire")
first = partial(multiply, 2) # partial function with 2 as the first parameter
print("This won't fire")       
second = partial(first, 3)        # partial function with 3 as the second parameter      
print(second(4))  # partial function with 4 as the third parameter and it will finally invoke the function


# use the multiprocessing library to calculate the fibonacci number
from multiprocessing import Pool

def fibonacci_mp(n):
    """This is a function that calculates the fibonacci number"""
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        fib = fibonacci_mp(n - 1) + fibonacci_mp(n - 2)
        print(f"Calculating fibonacci number {fib}")
        return fib

# use the multiprocessing library to calculate the fibonacci number
with Pool(processes=4) as pool:
    result = pool.map(fibonacci_mp, range(0, 10))
    print(result)
