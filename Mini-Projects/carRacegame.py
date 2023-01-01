# define the car class
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def race(self):
        print(f"{self.name} is racing at {self.speed} mph")


# create two cars
car1 = Car("Car 1", 200)
car2 = Car("Car 2", 180)

# start the race
car1.race()
car2.race()

# This code defines a Car class with a __init__ method that is called when a new Car object is created.
# The __init__ method takes two arguments: name and speed, which are used to initialize the object's attributes.
# The race method simply prints a message indicating the name and speed of the car.
# To start the race, we create two Car objects and call the race method on each of them.
# This will print two messages indicating the name and speed of each car.
