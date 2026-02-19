#Introduction to Python Dictionaries.

#In Python the dictionaries are key-value pairs. It is enclosed in curly brackets. Below is a simple example of Python Dictionaries:

programming_dictionary = {
    "bug" : "A mistake in program which is kind of difficult to find out.",
    "funtion" : "It is used to repeat the same piece of code multiple times.",
    "loop" : "Runs a program condition until it is broken by a valid condition.",
}

#Here, the dictionary name is "programming_dictionary". It has 3 different keys followed by 3 different values.

#Printing out the values of an associated key in dictionary:
# print(f"The value of Dictionary loop is: {programming_dictionary["loop"]}")

# print(programming_dictionary['loop'])

#Adding additional Key Value to exisiting dictionary:
# programming_dictionary["Python"] = "One of the most widely used Programming Language."

# #Printing out the new dictionary:
# print(programming_dictionary)

#The same way can be used to edit an existing Key and it's respective value:
# programming_dictionary["funtion"] = "Used to repeat a small block of code."

# print(programming_dictionary)

#Looping through a Dictionary:
# for thing in programming_dictionary:
#     print(thing)                   #Prints only the key names
#     print(programming_dictionary[thing]) #Prints the Values of Keys


#############################################################################################

#Nesting in Dictionaries:

#The value of Key can be anything - a List, or another Dictionary
#Each Key has only one value, if you want a key to have more than one value you have to make use of a List like shown below.
travel_log = {
    "France": ["Italy", "Dijon", "Lille"],
    "USA" : ["Ohio", "New Jersey", "Buffalo"]
}

# #Printing Lille from Key France:
# print(travel_log["France"][2])

# #Printing Character from Nested Lists:
# nested_list = ['A', 'B', ['C', 'D']]
# print(nested_list[2][1])

#Dictionary within a Dictionary:
travel_log = {
    "France": { 
        "number_of_times": 8,
        "total_cities_visited" : "2",
    },
    "USA" : ["Ohio", "New Jersey", "Buffalo"]
}

#Printing Values in Nested Dictionaries:
print(travel_log["France"]["total_cities_visited"])
