""" Classes in python """
class Dog:
    def __init__(self, name="", height="", weight=""):
        self.name = name
        self.height = height
        self.weight = weight
    
    def run(self):
        print("{} the dog runs".format(self.name))
    
    def barks(self):
        print("{} the dog barks".format(self.name))

def main():
    Bulldog = Dog("Bulldog", 65, 76)
    Bulldog.barks()

    Bowers = Dog("Bowers", 65, 27)
    Bowers.run()
main()

# Example 1

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        return(self.__height)
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Numbers allowed only")
    
    @property
    def width(self):
        return(self.__width)
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Numbers allowed only")

    def get_area(self):
        return int(self.__height) * int(self.__width)

#def main():
#    _Square = Square()
#
#   height = int(input("Enter the height: "))
#    width = int(input("Enter the width: "))
#
#    _Square.height = height
#    _Square.width = width
#
#    print("Height = ", _Square.height)
#    print("Width = ", _Square.width)
#    print("The Area = ", _Square.get_area())

#main()
# square needs to be debug

""" Inheritance magic method in python """

class Animal:
    def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
        self.birth_type = birth_type
        self.appearance = appearance
        self.blooded = blooded
    
    @property
    def birth_type(self):
        return self.__birth_type
    
    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type
    
    @property
    def appearance(self):
        return self.__appearance
    
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance
    
    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded
    
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birth_type, self.appearance, self.blooded)
    
class Mammals:
    def __init__(self, birth_type="born alive", appearance="hair or fur", blooded="warm-blooded", nurse_young=True):
        Animal.__init__(self, birth_type, appearance, blooded)
        self.nurse_young = nurse_young
        
    @property
    def nurse_young(self):
        return self.__nurse_young
    
    @nurse_young.setter
    def nurse_young(self, nurse_young):
        self.__nurse_young = nurse_young
        
    def __str__(self):
        return super().__str__() + " and it is {} who the nurse their young".format(self.nurse_young)

class Reptile(Animal):
    def __init__(self, birth_type="born in an egg", appearance="dry scales", blooded="cold-blooded"):
        Animal.__init__(self, birth_type, appearance, blooded)
    
    def sumAll(self, *args):
        sum = 0

        for x in args:
            sum += x
        return sum

def main():
    Animal_1 = Animal("born alive")
    print(Animal_1.birth_type)
    print(Animal_1)
    print()

    Mammals_1 = Mammals()
    print(Mammals_1.birth_type)
    print(Mammals_1.appearance)
    print(Mammals_1.blooded)
    print()

    Reptile_1 = Reptile()
    print(Reptile_1.birth_type)
    print(Reptile_1.appearance)
    print(Reptile_1.blooded)
    print()
main()

""" Static methods/ Exception handling """
# Example 1

class Sum:
    @staticmethod
    def get_sum(*args):
        sum = 0
        for x in args:
            sum += x
        return sum

def main():
    print("Sum = ", Sum.get_sum(1, 2, 4, 6, 8))
main()

# Example 2

class Dog:
    num_of_dogs = 0
    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1
    
    @staticmethod
    def get_dogs():
        print("There are {} number of dogs".format(Dog.num_of_dogs))
    
def main():
    Bulldogs = Dog("Bulldogs")
    puppy = Dog("puppy")

    Bulldogs.get_dogs()
    puppy.get_dogs
main()