""" Functions in python """
def mul(num_1, num_2): # creating a function
    #multiplication = num_1 * num_2
    return num_1 * num_2

print("4 * 3 = ", mul(4, 3))
print(mul(2, 3))

# Example 1
glb_name = "steve jobs" # global variable
def change_name():
    global glb_name
    glb_name = "John Njuguna"

change_name()
print(glb_name)

# Example 2
def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(4, 3)
print("4 * 3 = ", mult)
print("4 / 3 = ", divide)

# Example 3 => That prints prime numbers
def is_prime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True

def get_prime(max_num):
    list_prime = []
    for y in range(2, max_num):
        if is_prime(y):
            list_prime.append(y)
    return list_prime

max_number = int(input("Search for prime upto: "))
list_prime = get_prime(max_number)
for prime in list_prime:
    print(prime)

# Handle unknown arguments
def sum_all(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print("Sum = ", sum_all(2, 5, 6, 9, 10))