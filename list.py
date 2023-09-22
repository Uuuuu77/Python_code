""" Lists in python """
shopping_list = ["laptop", "chair", "cloths"]
print(shopping_list[0:1])
print(shopping_list[:2])
shopping_list[0] = "watch"
print(shopping_list)
print("Lenght = ", len(shopping_list))

my_list = shopping_list[0:3]
for x in my_list:
    print("{} = {}".format(shopping_list.index(x), x))

print(my_list.count("cloths"))

# Example 1
import random
random_list = []
for x in range(5):
    random_list.append(random.randrange(1, 7))
random_list.sort()
random_list.reverse() # more, like insert, pop, count, append...
for y in random_list:
    print(y)

# Example 2 Bubble sort
random_list = []
for x in range(5):
    random_list.append(random.randrange(1, 7))
z = len(random_list) - 1
while z > 1:

    zz = 0
    while zz < x:
        if random_list[zz] > random_list[zz + 1]:
            temp = random_list[zz]
            random_list[zz] = random_list[zz + 1]
            random_list[zz + 1] = temp
        else:
            print()
        zz += 1
    z -= 1

for y in random_list:
    print(y, end=" , ")
print()

""" List comprehensive """
even_list = [x * 2 for x in range(10)]
for x in even_list:
    print(x)

# Example 3 multiplication table
mult_table = [[0] * 10 for x in range(10)]
for x in range(1, 10):
    for y in range(1, 10):
        mult_table[x][y] = x * y

for x in range(1, 10):
    for y in range(1, 10):
        print(mult_table[x][y], end=" , ")
    print()