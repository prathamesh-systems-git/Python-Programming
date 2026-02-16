#Python Program to Calculate the Love Score between Two Given Names Using Function:

def calculate_love_score(name1, name2):
    #Combine the given 2 names & convert them to lowercase
    combined_names = (name1 + name2).lower()

    #Count Letters for TRUE
    true_score = (
        combined_names.count('t') +
        combined_names.count('r') +
        combined_names.count('u') +
        combined_names.count('e')
    )

    #Count Letters for LOVE
    love_score = (
        combined_names.count('l') +
        combined_names.count('o') +
        combined_names.count('v') +
        combined_names.count('e')
    )

    #Combine the 2 scores
    total_score = int(str(true_score) + str(love_score))

    print(f"The Love Score is {total_score}")

#Run the below if you do not require Inputs from user.
#calculate_love_score("Keanu", "Jennifer")

name1 = input("Enter Name of First Person: ")
name2 = input("Enter Name of Second Person: ")
print("Calculating Love Score...Please wait...")
calculate_love_score(name1, name2)



