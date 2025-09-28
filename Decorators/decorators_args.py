

def greet(fx):
    def wrapper(*args):
        print("Adding two numbers")
        fx(*args)
        print("Summation complete")
    return wrapper

@greet
def add(a,b):
    print(a+b)

add(6,7)