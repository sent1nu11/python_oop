class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
    
# create some book instances
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title 2", "COMIC")

