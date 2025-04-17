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