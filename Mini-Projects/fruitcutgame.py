# define the fruit class
class Fruit:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def cut(self):
        print(f"Cutting a {self.size}-inch {self.name}")


# create two fruits
fruit1 = Fruit("apple", 4)
fruit2 = Fruit("banana", 6)

# start cutting the fruits
fruit1.cut()
fruit2.cut()

# This code defines a Fruit class with a __init__ method that is called when a new Fruit object is created.
# The __init__ method takes two arguments: name and size, which are used to initialize the object's attributes.
# The cut method simply prints a message indicating the name and size of the fruit.
# To start cutting the fruits, we create two Fruit objects and call the cut method on each of them.
# This will print two messages indicating the name and size of each fruit.
