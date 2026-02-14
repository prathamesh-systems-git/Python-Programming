#Python Program to Print Random Number along with it’s Types:

import random
#Printing random number between range of 1 to 10:
random_number = random.randint(1,10)
print(random_number)

#Printing random decimal or floating number between range 0 and 1:
random_float_number = random.random()
print(random_float_number)

#Printing random floating number between specified range:
random_float_range = random.uniform(1,5)
print(random_float_range)
