# yotam greenstein 314856188
import math

class Point:
    def __init__(self, x=0, y=0): # __init__ is a saved word for a constructor in python, it is called when an object is created. It is like a constructor in C++.
        if not isinstance(x, (int, float)):    # isinstance(object, class_or_tuple or build in type) is used to check if the object is an instance of the class or tuple or build in type.
            raise TypeError('x should be an integer or float')
        if not isinstance(y, (int, float)):
            raise TypeError('y should be an integer or float')
        self.x = x  # self is like this in C++, unlike in c++ self is not passed as an hidden argument behind the scene.
        self.y = y

    def __str__(self): # f is used to format the string, it is called f-string. It is used to format the string in python.
        return f'({self.x},{self.y})'

    def __add__(self, other):
        """Adds either another Point or a scalar to this Point."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Operand must be a Point instance or a number (int or float)")

    def __sub__(self, other):
        """Subtracts either another Point or a scalar from this Point."""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):  # elif is used to handle a specific alternative case: if other is a number, add it to both coordinates.
            return Point(self.x - other, self.y - other)
        else: # serves as a safeguard for anything that doesn’t match either condition, enforcing strict type-checking and helping avoid unintended inputs.
            raise TypeError("Operand must be a Point instance or a number (int or float)")

    def __mul__(self, scalar):
        """Multiplies the Point's coordinates by a scalar."""
        if isinstance(scalar, (int, float)):
            return Point(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Scalar must be a number (int or float)")

    def __eq__(self, other):
        """Checks if two Points are equal."""
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __getitem__(self, key): # By implementing __getitem__ in a class, you allow instances of that class to support indexing and key access (like a list or dictionary). When you write my_object[key], Python automatically calls my_object.__getitem__(key).
        if key == 0 or key == 'x':
            return self.x
        elif key == 1 or key == 'y':
            return self.y
        else:
            raise KeyError("Key must be 0, 1, 'x', or 'y'")

    def __iter__(self): # iter is a special method that defines a class as iterable. When we implement it, objects of the class becomes iterables. 
        # A reserved word used to return values in sequence, one after another, without ending the function’s execution. It allows the creation of generator functions that return values in a loop, enabling us to yield values from the function each time it is called.
        yield self.x  # תחזיר את x
        yield self.y  # ואז את y

    def __len__(self):
        return 2

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)



