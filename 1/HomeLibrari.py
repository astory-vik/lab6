class HomeLibrari:
    books = []

    def AddBook(self, Book):
        self.books.append(Book)
        print(Book.Name + " added")

    def DeleteBook(self, BookName):
        k = 0
        for i in self.books:
            if i.Name == BookName:
                self.books.pop(k)

                print(i.Name + " deleted")
            k += 1

    def SearchBookByName(self, Name):
        for i in self.books:
            if i.Name == Name:
                print(i.Name + ' found')
                return i

    def SearchBookByAuthor(self, Author):
        for i in self.books:
            if i.Author == Author:
                print(i.Name + ' found')
                return i

    def SearchBookByYear(self, year):
        for i in self.books:
            if i.yearOfPublication == year:
                print(i.Name + ' found')
                return i
