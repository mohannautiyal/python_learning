import functools
import inspect

def decoratorfunc(func):
    @functools.wraps(func)
    def wrapper(*args):
        print("Printing before main func")
        func(*args)
        print("Printing after main func")
        print(f"arguments are {inspect.signature(func)}")
        # inspect.signature(func).bind(,*args)



















































    return wrapper

@decoratorfunc
def greetTest(name,country= None):
    print(f"Hello {name} from {country}")
    print(greetTest.__name__)

greetTest("Madan","India")