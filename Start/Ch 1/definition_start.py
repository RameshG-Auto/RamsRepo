# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title):
        self.title = title

# TODO: create instances of the class
book1 = Book("Seven Pillars of Wisdom")
book2 = Book("Lord of the Rings")

# TODO: print the class object and property
print(book1)
print(book1.title)
print(book2)
print(book2.title)