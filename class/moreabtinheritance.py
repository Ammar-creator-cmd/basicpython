class books:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
a_book = books("Sherlock Holmes", "Arthur Conan Doyle")
print(a_book.get_title())
print(a_book.get_author())


class fiction(books):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def get_genre(self):
        return self.genre
    
a_fiction_book = fiction("The Journey to the End of the Earth", "Jules Verne", "Adventure")
print(a_fiction_book.get_title())
print(a_fiction_book.get_author())
print(a_fiction_book.get_genre())

class non_fiction(books):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def get_subject(self):
        return self.subject
    
a_non_fiction_book = non_fiction("A Brief History of Time", "Stephen Hawking", "Science")
print(a_non_fiction_book.get_title())
print(a_non_fiction_book.get_author())
print(a_non_fiction_book.get_subject())
