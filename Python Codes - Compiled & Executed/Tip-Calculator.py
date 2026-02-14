#Python Program to Calculate Tip Each Person Has to Pay:

print("Welcome To The Tip Calculator...!!!")
total_bill = float(input("Enter Amount of Total Bill: "))
tip_amount = float(input("Enter Tip Amount: "))
number_of_peoples = int(input("How Many People Ate:? "))
total_tip_amount = float((total_bill * tip_amount) / 100)
new_total = float((total_bill + total_tip_amount) / number_of_peoples)
print(f"Each Person Has To Pay Rs.{new_total} Including Tip Amount.")
round_new_total = round(new_total)
print(f"Each Person Has To Pay Rs.{round_new_total} After Rounding Off.")
