# First Class Functions: Functions that can be passed around as arguments and/or returned from other functions

def square(x):
    return x * x

# f = square(5)
# print(square)
# print(f)

# f = square
# print(square)
# print(f)
# print(f(5))



# Higher Order Functions: Functions that take other functions as arguments or return them as results

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


def cube(x):
    return x * x * x


# num_list = [1, 2, 3, 4, 5]

# squares = my_map(square, num_list)
# print(squares)

# cubes = my_map(cube, num_list)
# print(cubes)



# Functions returning other functions

def logger(message):
    def log_message():
        # print(message)
        return message
    return log_message

# say_hi = logger('Hi')
# log_message = say_hi()
# print(log_message)



# 

def post_tag(tag):
    def build_tag_content(content):
        return f"<{tag}>{content}</{tag}>"
    return build_tag_content

# print_tag = post_tag('h1')
# created_block = print_tag('New tag posted')
# print(created_block)



# Closures: A closure is a function object that has access to variables in its enclosing scope even if the enclosing function is finished executing

def build_logger():
    message = 'Hi'

    def post_log():
        return message
    
    # return post_log()
    return post_log


# post_hi = build_logger()
# print(post_hi)
# print(post_hi.__name__)

# posted_log = post_hi()
# print(posted_log)


# Free variable: 
def outer_func(msg):
    # free variable
    message = msg

    def inner_func():
        print(message)
    return inner_func


# say_hi = outer_func('hi')
# say_hello = outer_func('hello')
# say_hi()
# say_hello()


# Example of a closure: Custom Logger Decorator

import logging
logging.basicConfig(level=logging.INFO)

def logger_wrapper(func: callable):
    def logger_modifier(*args):
        logging.info(f"Running '{func.__name__}' with args {args}")
        print(func(*args))
    return logger_modifier


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# add_logged = logger_wrapper(add)
# print(add_logged)
# add_logged(3, 3)

# multiply_logged = logger_wrapper(multiply)
# print(multiply_logged)
# multiply_logged(3, 3)




# Decorators: A decorator is just a function that takes another function as an argument, adds some kind of functionality and then returns another function

def decorated_function(original_function: callable):
    def wrapper_function(*args, **kwargs):
        print(f"The wrapper function executed and printed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorated_function
def display():
    print('Display function run')


# decorated_display = decorated_function(display)
# decorated_display()

# display = decorated_function(display)
# display()


@decorated_function
def display_info(age: int, name: str):
    print(f"Age: {age}, Name: {name}")


# display()
# display_info(35, 'John')



# Class Decorators

class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"The wrapper class executed and printed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_info(age: int, name: str):
    print(f"Age: {age}, Name: {name}")


# display_info(35, 'John')



# USEFUL DECORATORS

# Logging decorator

from functools import wraps

def logger_decorator(original_func: callable):
    import logging
    logging.basicConfig(level=logging.INFO)
    
    @wraps(original_func)
    def wrapper_function(*args, **kwargs):
        logging.info(f"Calling {original_func.__name__} with args: {args} and kwargs: {kwargs}")
        return original_func(*args, **kwargs)
    return wrapper_function


# Timing decorator

def timing_decorator(original_function: callable):

    @wraps(original_function)
    def timer_wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = original_function(*args, **kwargs)
        run_time = time.time() - start_time
        print(f"{original_function.__name__} finished in {run_time}")
        return result
    return timer_wrapper


@logger_decorator
@timing_decorator
def display_info(age: int, name: str):
    print(f"Age: {age}, Name: {name}")


# display_info(34, 'Anna')



def fibonacci(n: int):
    # base case
    if n in (0, 1):
        return n
    
    # recursion case
    return fibonacci(n-1) + fibonacci(n-2)

# timed_fibonacci = timing_decorator(fibonacci)
# print(timed_fibonacci(9))

# print(fibonacci(9))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))
# print(fibonacci(8))



# Decorators with parameters

def decorator_with_args(param):
    def logger_decorator(original_func):
        def wrapper(*args, **kwargs):
            print(f"Calling {original_func.__name__} with args: {args} and kwargs: {kwargs}")
            print(f"Calling {original_func.__name__} with decorator parameter: {param}")
            return original_func(*args, **kwargs)
        return wrapper
    return logger_decorator


@decorator_with_args('TESTING decorator parameters')
def display_info(age: int, name: str):
    print(f"Age: {age}, Name: {name}")


display_info(34, 'Anna')