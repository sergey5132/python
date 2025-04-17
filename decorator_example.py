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




