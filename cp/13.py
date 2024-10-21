class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author =author
        self.pages = pages
    def get_summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
class EBook (Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size
    def get_summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages, {self.file_size}MB"
ebook = EBook ("GOD'S PLAN", "GOD", 9999, 10000)
print(ebook.get_summary())
print("Project by DHRUV GUPTA, 2024UCI8045")
