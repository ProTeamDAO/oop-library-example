# import classes from files
from book import Book
from library import Library

# creating Book objects
book1 = Book('Lord of the Rings', '435fsdfs')
book2 = Book('Python for everybody', '1234dsf')

# creating Library objects
library1 = Library('National Library', 'Warsaw, Grzybowska 12')
library2 = Library('Super Library', 'Ankara, Kedi 12')

print(book1.title)