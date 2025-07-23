#  Декораторы — это функции, которые принимают другую функцию в качестве аргумента и возвращают новую функцию, изменяя или расширяя поведение исходной функции. Декораторы используются для повышения удобочитаемости и повторного использования кода.
#
# Декораторы позволяют модифицировать поведение функций или методов без изменения их исходного кода. Поэтому они широко используются для добавления функциональности, логирования, контроля доступа и многих других задач.
#
# Синтаксис декораторов в Python включает использование символа @ перед именем декоратора, который размещается перед определением функции.

import time

def log_decorator(func):
    def wraper():
        print("start")
        func()
        print("end")

    return wraper

@log_decorator
def greet():
    print('Hello')

greet()

# многоуровневый декортатор
def repeat(num_times):
    def repeat_dec(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return repeat_dec


@repeat(num_times=3)
def say_hello(name):
    print(f'Hello {name}')


say_hello('Alex')

class MyDecorator:
    @staticmethod
    def static_metod():
        print("Это статический метод")

MyDecorator.static_metod()

def log_call(func):
    def wrapper(*args,**kwargs):
        print(f'вызов функции {func.__name__} с параметрами {args} ')
        return func(args)
    return wrapper

@log_call
def add_num(x,y):
    print(x + y)
    return x + y

# print(add_num(1,2))
def duration(func):
    def wrapper(args):
        print(time.time())
        res=func(args)
        print(time.time())
        return res
    return  wrapper

def cache(func):
    result_cache = {}
    def wrapper(args):
        if args in result_cache:
            print('yes')
            return result_cache[args]
        result=func(args)
        result_cache[args]=result
        print('no')
        return result
    return wrapper
@duration
@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

