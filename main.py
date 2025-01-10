# Book class definition
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
    
    
# Library class definition
class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address


# creating Book objects
book1 = Book('Lord of the Rings', '435fsdfs')
book2 = Book('Python for everybody', '1234dsf')

# creating Library objects
library1 = Library('National Library', 'Warsaw, Grzybowska 12')
library2 = Library('Super Library', 'Ankara, Kedi 12')

print(book1.title)