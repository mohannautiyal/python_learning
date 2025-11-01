def decoratorfunc(func):
    def wrapper():
        print("Printing before main func")
        func()
        print("Printing after main func")
    return wrapper()

@decoratorfunc
def greetTest():
    print("Hello Test A ")

