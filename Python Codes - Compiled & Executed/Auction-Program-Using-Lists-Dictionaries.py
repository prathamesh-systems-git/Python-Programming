#Python Program to Create an Auction Program:

print("Let the Auction Begin...!!!")

#Saving the Name and Bid Amount in Empty Dictionaries:
bid_names = { }

#Defining a Function to Compare the Bids:
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    
    print(f"The Winner is {winner} with a Bid Amount of ${highest_bidder}")

#Getting confirmation for any new Bids before declaring the Winner:

continue_bidding = True
while continue_bidding:
    print(" ")
    your_name = input("What is your Name? ")
    your_bid = int(input("What is your Bid Amount? "))
    print(" ")
    bid_names[your_name] = your_bid
    end_bid = input("Does anyone want to Bid? (Yes/No): ").lower()
    if end_bid == "no":
        continue_bidding = False
        find_highest_bidder(bid_names)
    elif end_bid == "yes":
        print("\n" * 100)

