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

""" Recursive functions """
# Dictionaries in python
name = {"fname": "john", "lname": "njuguna", "address": "baraka, nairobi"}
print("my name = ", name["fname"])
print(name.keys())
print(name.values())
name["country"] = "Kenya"
print(name["country"])
del[name["address"]]
for k, v in name.items():
    print(k, v)

# recusive functiom
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result
    
print("5! = ", factorial(5))

# Example on fibonnaci
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result
    
print(fib(3))
print(fib(4))
print(fib(5))