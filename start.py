class Book:
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        # TODO: ad properties
        self.title = title
        self.pages = pages
        self.price = price

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount
    
# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: print the price of book2
print(b2.getprice())
b2.setdiscount(0.25)

print(b2.getprice())
