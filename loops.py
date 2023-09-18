""" For loop in python """
for x in [1,3,5,7,9]: # Cycling through a list
    print("x = {}".format(x))

for y in range(10): # Range function used in for loop
    print("y = {}".format(y))
for z in range(2, 10, 2):
    print("z = {}".format(z))

""" Check for even numbers in for loop """
for b in range(20):
    if ((b % 2) == 0):
        print("b = {}".format(b))


""" While loop in python """
import random
rand_num = random.randrange(0, 21)

x = 0
while (x != rand_num):
    x += 1

print("Random number is: {}".format(rand_num))
