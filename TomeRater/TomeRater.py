#USER CLASS

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, updated_email):
        self.email = updated_email
        return "Email updated to: {email}".format(email=updated_email)

    def __repr__(self):
        return "Registered as: {name}, Email: {email}, Number of Books Read: {books}."\
               .format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email 

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)
    
    def get_book_read_count(self):
        return len(self.books)

    def __hash__(self):
        return hash((self.name, self.email))

#BOOK CLASS

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "Title: '{title}', ISBN: {isbn}".format(title=self.title, isbn=self.isbn)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, updated_isbn):
        self.isbn = updated_isbn
        return "This book's ISBN has been updated to: {isbn}".format(isbn=updated_isbn)

    def add_rating(self, rating):
        if (rating in range(0,5)):
            self.ratings.append(rating)
        else:
            print("None is an Invalid Rating.  Please Use 0 to 4.")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))


#FICTION SUBCLASS of BOOK

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "Title: {title}, By: {author}, ISBN: {isbn}".format(title=self.title, author=self.author, isbn=self.isbn)


#NON-FICTION SUBCLASS of BOOK

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "Title: {title}, Level: {level}, On Subject: {subject}, ISBN: {isbn}"\
            .format(title=self.title, level=self.level, subject=self.subject, isbn=self.isbn)


#TOMERATER CLASS!!

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email: {email}".format(email=email))
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book, 0) + 1

    def add_user(self, name, email, books=None):
        if email not in self.users:
            self.users[email] = User(name, email)
            if books is not None:
                for book in books:
                    self.add_book_to_user(book, email)
        else:
            print("User Exists!")

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')

    def most_positive_user(self):
        highest_rated = max(rating.get_average_rating() for rating in self.users.values())
        return str([user for user in self.users.values() if user.get_average_rating() == highest_rated]).strip('[]')



