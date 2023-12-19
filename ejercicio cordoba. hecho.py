class Publication:
    def __init__(self, title, authors, year, status="available"):
        self.title = title
        self.authors = authors
        self.year = year
        self.status = status


class Book(Publication):
    def __init__(self, title, authors, year, ISBN, num_pages):
        super().__init__(title, authors, year)
        self.ISBN = ISBN
        self.num_pages = num_pages


class Journal(Publication):
    def __init__(self, title, authors, year, edition_num, periodicity):
        super().__init__(title, authors, year)
        self.edition_num = edition_num
        self.periodicity = periodicity


class User:
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
        self.pubs = []

    def lend_pub(self, publication):
        self.pubs.append(publication)
        publication.status = "borrowed"

    def return_pub(self, publication):
        if publication in self.pubs:
            self.pubs.remove(publication)
            publication.status = "available"


class Professor(User):
    def __init__(self, name, userID, department, employeeID, max_pubs=2):
        super().__init__(name, userID)
        self.department = department
        self.employeeID = employeeID
        self.max_pubs = max_pubs


class Student(User):
    def __init__(self, name, userID, grade, studentID, max_pubs=1):
        super().__init__(name, userID)
        self.grade = grade
        self.studentID = studentID
        self.max_pubs = max_pubs


class Library:
    def __init__(self, name):
        self.name = name
        self.catalogue = []
        self.users = []

    def show_catalog(self):
        for publication in self.catalogue:
            print(publication.title)

    def add_publication(self, publication):
        self.catalogue.append(publication)

    def register_user(self, user):
        self.users.append(user)

    def lend_pub(self, user, publication):
        if user in self.users and publication in self.catalogue:
            if publication.status == "available" and len(user.pubs) < user.max_pubs:
                user.lend_pub(publication)
                publication.status = "borrowed"
                print(f"{user.name} has borrowed '{publication.title}'")
            else:
                print("Publication is not available or user has reached the maximum limit of publications.")

    def return_pub(self, user, publication):
        if user in self.users and publication in self.catalogue:
            if publication.status == "borrowed" and publication in user.pubs:
                user.return_pub(publication)
                publication.status = "available"
                print(f"{user.name} has returned '{publication.title}'")
            else:
                print("Publication is not borrowed by the user or not available in the catalogue.")


# Example Usage
library = Library("Loyola Andalucía Library")

book1 = Book("Learning Python II", ["Javier Perez", "Daniel Muñoz"], 2023, "1234567890123", 300)
journal1 = Journal("Technology Journal", ["Stephen Curry", "LeBron James"], 2022, 7, "Annual")
journal2 = Journal("Medical Journal", ["Michael Jordan", "Larry Bird"], 2023, 5, "Monthly")

professor1 = Professor("Professor Tija", "123456789", "Philosophy", "123456")
student1 = Student("Ashkabos Teberio", "987654321", "DAN", "654321")
student2 = Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")

library.add_publication(book1)
library.add_publication(journal1)
library.add_publication(journal2)

library.register_user(professor1)
library.register_user(student1)
library.show_catalog()

library.lend_pub(professor1, book1)
library.lend_pub(student1, book1)  # the book should be borrowed
print(student1.pubs)  # empty list

library.return_pub(professor1, book1)
library.lend_pub(student1, book1)  # the book should be available now
library.lend_pub(student1, journal2)
print(student1.pubs)

library.lend_pub(student2, journal1)  # User not registered

