class Book:
    Name = "";
    Author = "";
    Genre = "";
    yearOfPublication = 0;
    def __init__(self,name, author, genre, yearOfPublication):
        self.Name = name;
        self.Author = author
        self.Genre = genre
        self.yearOfPublication = yearOfPublication
