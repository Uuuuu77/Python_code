""" Basic syntax of string """
name = "john njuguna"
print(name.upper())
print(name)

print(name.find("g"))

print(name.replace("j", "J"))

""" Math string Exception Handling """
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a number of your age")
    except:
        print("Unknown error")
print("your age is {}".format(age))

# Example 1
secret_number = 6

while True:
    try:
        guess = int(input("Enter number btwn 0 to 10 "))

        if guess == secret_number:
            print('Congratulation, you guessed it!')
            break
    except:
        print("Unknown Error")

""" Math Module """
import math
# log, factorial, absolute(abs), module(fmod)...

""" String """
print(type(2)) #int
print(type("john")) #string
print(type(4.35)) #float

my_string = "Congratulation!"
print(my_string)
print(my_string[0])
print(my_string[-1])
print(len(my_string))
print(my_string[1:13])

for x in my_string:
    print("X = ", x)

################################

""" String Function """
import sys
random_string = "  congratulations  "
random_string = random_string.lstrip()
random_string = random_string.rstrip()
random_string = random_string.strip
#print(random_string.lstrip()) needs to debug
#print(random_string.capitalize())
#print(random_string.upper())
#print(random_string.lower())
#print("Count string = ", random_string.count())
#print(random_string.split(" "))

# some of the string function include: islower, isupper, isdigit, isalpha, isalpnum...