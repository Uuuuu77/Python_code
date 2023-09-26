print("Hello world!")
#My first statement in python

""" File input/output in python """
import os
with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("some data\nmore data\nand some more data")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)
print(my_file.name)
print(my_file.mode)

with open("mydata.txt", encoding="utf-8") as my_file:
    lineNum = 1

    while True:
        line = my_file.readline()
        if not line:
            break
        print("lineNum ", lineNum, " : ", line, end="")
    lineNum += 1


