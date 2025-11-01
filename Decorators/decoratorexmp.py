import functools


def greet(fx):
    @functools.wraps(fx)
    def wrapper():
        print("Good Morning")
        fx()
        print("Good Night")
    return wrapper


@greet
def sayHello():
    print("Hello")
    print(sayHello.__name__)


# sayHello()
#
# f=greet(sayHello)
# f()
# sayHello()
