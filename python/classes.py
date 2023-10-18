# Notes: 
#      __str__: Returns text used as a string representation of an object.
#      __repr__: Returns text used as a more detailed representation of an object.
#      __eq__: Checks whether two objects are equal.
#      __ne__: Checks that two objects are not equal.
#      __hash__: Returns a hash of the object.

class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"
    
    def __str__(self):
        return "A {} vehicle with {} doors and {} tires".format(self.color, self.doors, self.tires)
    
    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(self.__class__.__name__, self.color, self.doors, self.tires)
    
    def __eq__(self, other):
        return self.color == other.color and self.doors == other.doors and self.tires == other.tires
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.color, self.doors, self.tires))

class Car(Vehicle):
    """The Car class"""
    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"
    
    def drive(self):
        return "I'm a car!"
    
    def __str__(self):
        return "A {} car with {} doors and {} tires".format(self.color, self.doors, self.tires)
    
    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(self.__class__.__name__, self.color, self.doors, self.tires)
    
    def __eq__(self, other):
        return self.color == other.color and self.doors == other.doors and self.tires == other.tires
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.color, self.doors, self.tires))
    
class Truck(Vehicle):
    """The Truck class"""
    def drive(self):
        """
        Override drive method
        """
        return "I'm a truck and I'm driving slowly because I'm heavy!"
    
    def __str__(self):
        return "A {} truck with {} doors and {} tires".format(self.color, self.doors, self.tires)
    
    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(self.__class__.__name__, self.color, self.doors, self.tires)
    
    def __eq__(self, other):
        return self.color == other.color and self.doors == other.doors and self.tires == other.tires
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.color, self.doors, self.tires))
    
if __name__ == "__main__":
    car = Car("blue", 5, 4)
    print("1",car)
    truck = Truck("red", 3, 6)
    print("2",truck)
    print("3",car.drive())
    print("4",truck.drive())
    print("5",car.brake())
    print("6",truck.brake())
    print("7",car == truck)
    print("8",car != truck)
    print("9",hash(car))
    print("10",hash(truck))
    print("11",car.__dict__)
    print("12",truck.__dict__)
    print("13",car.__class__)
    print("13",truck.__class__)
