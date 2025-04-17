#  Декораторы — это функции, которые принимают другую функцию в качестве аргумента и возвращают новую функцию, изменяя или расширяя поведение исходной функции. Декораторы используются для повышения удобочитаемости и повторного использования кода.
#
# Декораторы позволяют модифицировать поведение функций или методов без изменения их исходного кода. Поэтому они широко используются для добавления функциональности, логирования, контроля доступа и многих других задач.
#
# Синтаксис декораторов в Python включает использование символа @ перед именем декоратора, который размещается перед определением функции.



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




