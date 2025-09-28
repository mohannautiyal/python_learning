def greet(fx):
    def wrapper():
        print("Good Morning")
        fx()
        print("Good Night")
    return wrapper


@greet
def sayHello():
    print("Hello")

# sayHello()
#
# f=greet(sayHello)
# f()
sayHello()
