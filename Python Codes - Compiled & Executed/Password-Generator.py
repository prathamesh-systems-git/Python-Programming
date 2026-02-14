#Python Program to Create a Password Generator:
#Importing the Random Function
import random

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["@", "#", "$", "%", "&"]
password = []
print("Welcome to Python Random Password Generator.")
number_of_letters = int(input("How Many Letters You Want in Your Password? "))
number_of_numbers = int(input("How Many Numbers You Want in Your Password? "))
number_of_symbols = int(input("How Many Symbols You Want in Your Password? "))

for letters in range(1,number_of_letters + 1):
    password.append(random.choice(alphabets))

for nums in range(1,number_of_numbers + 1):
    password.append(random.choice(numbers))

for symb in range(1,number_of_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

print(password)

final_password = ""
for characters in password:
    final_password = final_password + characters

print(final_password)
