class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
book= Book("How to win heart", "Anamika Verma", 350)
print(book.get_summary())
print("Book attribution project by DHRUV GUPTA, 2024UCI8045")
