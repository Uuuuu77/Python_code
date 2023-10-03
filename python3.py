""" List Comprehension, Generators expression/functions, iterables """
# Example on iterator & iterables
sample_str = iter("Sample")
print("Char = ", next(sample_str))
print("Char = ", next(sample_str))

class alpha:
    def __init__(self):
        self.letter = "ABCDEFGHIJKFNOPUVWXYZ"
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.letter) - 1:
            raise StopIteration
        self.index += 1
        return self.letter[self.index]

alp = alpha()
for x in alp:
    print(x)


class fib_generator:
    def __init__(self):
        self.first = 0
        self.second = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum
fib_seq = fib_generator()
for x in range(10):
    print("Fib = ", next(fib_seq))

################################################

# Example on list comprehension
print(list(map((lambda x: x * 2), range(1, 11))))
print([2 * x for x in range(1, 11)])
print([x for x in range(1, 11) if x % 2 != 0])
print([x ** 2 for x in range(50) if x % 8 == 0])

import random
print([x for x in [random.randint(1, 1001) for y in range(50)] if x % 9 == 0])