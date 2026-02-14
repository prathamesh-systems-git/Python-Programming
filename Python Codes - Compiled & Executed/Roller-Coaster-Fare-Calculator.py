#Python Project using Nested If-Else Statement:

print("Welcome to the Roller-Coaster Ride.!")
height = int(input("Enter Your Height: "))
age = int(input("Enter Your Age: "))
amount = 50
if height >= 120:
    print("You can ride the rollercoaster.")
    if age >= 18 and age <= 30:
        print(f"Your total amount is {amount}")
    elif age > 30 and age <=50:
        amount = amount + 70
        print(f"Your total amount is {amount}")
    else:
        print(f"Since you are over 50 years of age, due to health reasons no roller-coaster ride for you.")
else:
    print("You cannot ride the rollercoaster.")
