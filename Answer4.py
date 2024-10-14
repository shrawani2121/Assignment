class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Making the class iterable
    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

# Example 
if __name__ == "__main__":
    rect = Rectangle(10, 20)

    # Iterating over the rectangle instance
    for dimension in rect:
        print(dimension)
