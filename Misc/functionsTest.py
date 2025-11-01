def welcome(guest_name):
    return f"Welcome {guest_name}"

# welcome_var = welcome("Madan")
# print(welcome_var)

def displayString(func,arg1):
    text_to_disp =func(arg1)
    print(text_to_disp)


displayString(welcome,"Rajesh")