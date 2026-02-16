#Python Program to show working of Positional Arguments & Keyword Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's the weather in {location}")

#Printing the below line in normal way
greet_with("Prathamesh", "Switzerland\n")

#Printing the below line using Positional Arguments
greet_with("Switzerland", "Prathamesh\n")

#Printing the same line using Keyword Arguments
greet_with(name= "Prathamesh", location = "Switzerland")
