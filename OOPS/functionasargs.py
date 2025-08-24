# Pass functions as arguments

def add(x,y):
    return x + y


# print(add(4,5))

def avg(func,x,y):
    sum = func(x,y)
    return sum/2

avg1 = avg(add,5,6)
print(avg1)