import inspect

def add(a,b):
    print("Adding two numbers")
    return a+b

print(add(4,5))
print(inspect.getsource(add))