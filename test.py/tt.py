from ast import Expression


def new_func():
    x = input("Enter an Expression: ")
    print("Answer:", eval(x))

new_func()