class Point:
    def __init__(self, x=0, y=0): # __init__ is a saved word for a constructor in python, it is called when an object is created. It is like a constructor in C++.
        self.x = x # self is like this in C++, unlike in c++ self is not passed as an hidden argument behind the scene.
        self.y = y
        if not isinstance(x,(int,float)):    # isinstance(object, class_or_tuple or build in type) is used to check if the object is an instance of the class or tuple or build in type.
            raise TypeError('x should be an integer')
        if not isinstance(y, (int,float) ):
            raise TypeError('x should be an integer')
    
    def point_name(self):
        return f'Point({self.x},{self.y})' # f is used to format the string, it is called f-string. It is used to format the string in python.

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y

    def addition(self,other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

        elif isinstance(other,(int,float)): # elif is used to handle a specific alternative case: if other is a number, add it to both coordinates.
            return Point(self.x + other, self.y + other)

        else:  # serves as a safeguard for anything that doesn’t match either condition, enforcing strict type-checking and helping avoid unintended inputs.
             raise TypeError("Other must be a Point instance or a number (int or float)")
    
    def substraction(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int,float)):
            return Point(self.x - other, self.y - other)
        else:
            raise TypeError("Other must be a Point instance or a number (int or float)")


    def multiply(self, scalar):
        if isinstance(scalar,(int,float)):
            return Point(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("scalar must be a number (int or float)")
         
    
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
