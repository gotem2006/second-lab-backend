"""Backend second lab."""
from typing import List
import time

# func without parametrs
def print_helloworld() -> None:
    """Function printing hello world."""
    print("Hello world")

#func with parametrs
def sum_of_twonumbers(a: int, b: int) -> int:
    """Function returns sum of two numbers."""
    return a + b

def multiply_array(array: List[int] = [1, 2, 3], multiply: int = 2) -> List[int]:
    """Function multiply all el in array."""
    for idx in range(len(array)):
        array[idx] = array[idx]*multiply
    return array

def sum_numbers(*args) -> int:
    """sum."""
    return sum(args)

def info(**kwargs):
    """info."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def sum_caller(*args):
    print("call sum")
    sum_numbers(args)

def time_work(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(end_time - start_time)

def do_func(func, *args):
    func(args)

def combine_func(f1, f2, value):
    return f1(f2(value))

def calculator(a, b):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    return add(a, b), subtract(a, b)

def greeting_creator():
    def formal_greet(name):
        return f"Good day, {name}."
    def casual_greet(name):
        return f"Hey {name}, what's up?"
    return formal_greet, casual_greet

def multiplier(factor):
    def multiply_by(value):
        return value * factor
    return multiply_by

def greeting_maker(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

def main() -> None:
    """Main."""
    time_work(multiply_array)
    print(calculator(1, 2))

    f1 = lambda: "Hello from lambda!"
    print(f1())
    f2 = lambda a, b: a + b
    print(f2(1, 2))
    f3 = lambda f: f(1, 2)
    print(f3(lambda a, b: a * b))

if __name__ == '__main__':
    main()
