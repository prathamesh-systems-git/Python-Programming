#Python Program using Function & Input from User:

def print_name():
    user_name = input("Enter Your Name: ")
    return user_name

name = print_name()
print(f"You have entered your name as {name}")
