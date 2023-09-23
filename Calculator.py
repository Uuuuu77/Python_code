# Building Calculator using python
num_1, operator, num_2 = input("Enter number: ").split()

num_1 = int(num_1) # Converts to integer
num_2 = int(num_2) # converts to integer

if operator == "+":
    print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
elif operator == "-":
    print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
elif operator == "*":
    print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
elif operator == "/":
    print("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
else:
    print("Enter the correct operator{+, -, *, /}")
    