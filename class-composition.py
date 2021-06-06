# Composition is a counterpart to inheritance.


class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books."


shelf = BookShelf(300)
print(shelf)


# Now if we want to create a Book class, some new programmers has maybe attempted to make it inherit from BookShelf. After all, they are somehow related. Book live in BookShelf. And then we would do something like bottom.
class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


# Now, why is this a bad approach? There are two reasons. One of them is conseptual, the way of thinking about it. The other one is technical. The conseptual reason is that when you do inheritance, you are essentially treating it like evolutionary inheritance. You are saying a Book is a BookShelf and something more. So here we are saying all Books are BookShelfs but not all BookShelfs are Books. So that breaks down, because a Book is something completely different from a BookShelf. A BookShelf can contain Books, but one isn't the other. The technical reason is that you got this Book class that inherits from Bookshelf, but actually you are not using inside it anything about the BookShelf. And we are completely overwriting the __str__ method. And we actually don't need Line 19 at all, because what's the point of setting the quantity if you are not going to use it in the methods? So the conseptual reason is a Book is not a BookShelf and the technical reason is there is no reason to inherit if you're not gonna use that inheritance anywhere.
book = Book("Harry Potter", 200)
print(book)


# So this is where composition comes in. Composition is for when you wanna say something like, a BookShelf has many Books. A BookShelf is composed of a bunch of things and books. So we do somethig like bottom. This is composition and this is very common. It is when you have a class that contains a bunch of other classes. 


class BookShelfCompose:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class BookCompose():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


book1 = BookCompose("Game Of Thrones")
book2 = BookCompose("The Lord of the Rings")

shelfcompose = BookShelfCompose(book1, book2)
print(shelfcompose)

# Also note that we can now access shelfcompose.books and that gives us all the books stored within the shelfcompose.

print(shelfcompose.books)

print(shelfcompose.books[0])
print(shelfcompose.books[1])

print(shelfcompose.books[0].name)
print(shelfcompose.books[1].name)