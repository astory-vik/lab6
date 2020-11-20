from HomeLibrari import HomeLibrari
from Book import Book


def Main():
    b1 = Book("Romeo and Juliet", "Shakespeare", "Roman", "1597")
    b2 = Book("Game of Thrones", "Martin", "Epic fantasy", "1996")
    b3 = Book("Harry Potter", "Roiling", "Roman", "1997")
    b4 = Book("War and peace", "Tolstoi", "Roman", "1867")
    mylibrary = HomeLibrari()
    mylibrary.AddBook(b1)
    mylibrary.AddBook(b2)
    mylibrary.AddBook(b3)
    mylibrary.AddBook(b4)
    mylibrary.SearchBookByName('Harry Potter')
    mylibrary.SearchBookByAuthor("Martin")
    mylibrary.SearchBookByYear('1997')

    mylibrary.DeleteBook('Romeo and Juliet')



if __name__ == '__main__':
    Main()