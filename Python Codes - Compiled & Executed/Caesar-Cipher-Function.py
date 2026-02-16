#Python Program to Create a Caesar Cipher to Encrypt & Decrypt the Input Message:

#Defining the A to Z Alphabet List:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

users_action = input("Choose Your Action: (Encrypt / Decrypt) - ").lower()
plain_text = input("Type Your Message: ").lower()
#Asking the user how many shifts are required
shift = int(input("Enter the Shift Number / Place: "))


#Creating a Function called encrypt() that takes original_text and shifts it as required:
def encrypt(original_text, shift_number):
    #Defining an empty string to collect the new Shifted Position Alphabet
    cipher_text = ""

    for letter in original_text:
        #Shifts the each letter of text to mentioned Shift number
        shifted_position = (alphabet.index(letter) + shift_number) % 26  #If shift goes beyond z, your code will crash. Hence, adding % 26
        cipher_text = cipher_text + alphabet[shifted_position]

    #Display the Encyrpted Text on screen
    print(f"Encrypted Result is: {cipher_text}")



#Creating a Function called decrypt to Decode the Plain Text:
def decrypt(original_text, shift_number):
    #Defining an empty string to collect the new Shifted Position Alphabet
    decipher_text = ""

    for letter in original_text:
        #Shifts the each letter of text to mentioned Shift number
        shifted_position = (alphabet.index(letter) - shift_number) % 26  #If shift goes beyond z, your code will crash. Hence, adding % 26
        decipher_text = decipher_text + alphabet[shifted_position]

    #Display the Encyrpted Text on screen
    print(f"Decrypted Result is: {decipher_text}")

#Deciding where the Function goes based on User's Action
if users_action == "encrypt":
    encrypt(original_text=plain_text, shift_number=shift)
elif users_action == "decrypt":
    decrypt(original_text=plain_text, shift_number=shift)
else:
    print("Wrong Input Provided...!!! Try Again!!! ")
    exit

