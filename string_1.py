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

# Unicode/ascii value
print("A = ", ord(A))
print("65 = ", chr(65))