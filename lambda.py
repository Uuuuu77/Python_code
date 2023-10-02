# Example 1
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    odd_list = []
    for x in list:
        if func(x):
            odd_list.append(x)
    return odd_list

alist = range(1, 20)
print(change_list(alist, is_odd))

# Example 2
sum = lambda x, y: x + y
print("Sum = ", sum(5, 5))

can_vote = lambda age: True if age >= 18 else False
print("Can vote ", can_vote(18))

import random
flip_list = []
for x in range(1, 101):
    flip_list += random.choices(["H", "T"])

print("Heads = ", flip_list.count("H"))
print("Tails = ", flip_list.count("T"))

# Map function
oneTo10 = range(1, 10)
def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneTo10)))
print(list(map((lambda x: x * 3), oneTo10)))