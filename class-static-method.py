class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


test = ClassTest()

# Note that both of these things are exactly the same.
test.instance_method()
ClassTest.instance_method(test)

test.class_method()
# Also note that we no longer need an instance like <test> for calling a class method.
ClassTest.class_method()
# Python itself will actually do this: ClassTest.class_method(ClassTest)


# Static method don't get either of self or cls. And we can call them with or without our instance object.
test.static_method()
ClassTest.static_method()


# Our Factory Example:

class Book:
    # We can use variables inside our classes. Here, this is a class property.
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weigth):
        self.name = name
        self.book_type = book_type
        self.weigth = weigth

    def __repr__(self):
        # The !r, calls the repr method of self.name and self.book_type here, so that it shows up as having the quotes ('') already. So this is just a little bit nicer that putting the qoutes in yourself.
        return f"Book({self.name!r}, {self.book_type!r}, {self.weigth})"

    @classmethod
    def hardcover(cls, name, page_weigth):
        return cls(name, cls.TYPES[0], page_weigth)

    @classmethod
    def paperback(cls, name, page_weigth):
        return cls(name, cls.TYPES[1], page_weigth)


print(Book.TYPES)

hobbit = Book("Hobbit", "hardcover", 2500)
print(hobbit)

# We want to only create books that are either hardcover or paperback in this class. But we can create a comic book here. So how can we solve this problem?
xmen = Book("X Men", "Comic Book", 500)
print(xmen)

# For solving this problem we can create two classmethod like above and then note that we no longer need to create our own object first (Like creating hobbit) and we can use those classmethods for creating our objects.
harrypotter = Book.hardcover("Harry Potter", 2000)
print(harrypotter)

python_101 = Book.paperback("Python 101", 400)
print(python_101)
