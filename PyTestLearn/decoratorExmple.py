
def wishmodified(func):
    def wishmodimpl(nameinput):
        if nameinput == "Kavya" :
            print("Hello "+nameinput+ " you are the best")
        else:
            func(nameinput)
    return wishmodimpl


@wishmodified
def wish(name):
    print("Hello "+name+ " How are you")

# decoratedWish = wishmodified(wish)


wish("Kavya")
