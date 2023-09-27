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

def main():
    _Square = Square()

    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))

    _Square.height = height
    _Square.width = width

    print("Height = ", _Square.height)
    print("Width = ", _Square.width)
    print("The Area = ", _Square.get_area())

main()
# square needs to be debug