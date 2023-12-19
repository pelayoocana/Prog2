library = Library("Loyola Andalucía Library")
book1 = Book("Learning Python II",
["Javier Perez", "Daniel Muñoz"],
2023, "1234567890123", 300)
journal1 = Journal("Technology Journal",
["Stephen Curry", "LeBron James"],
2022, 7, "Annual")
journal2 = Journal("Medical Journal",
["Michael Jordan", "Larry Bird"],
2023, 5, "Monthly")
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
library.lend_pub(student1, book1) # the book should be borrowed
print(student1.pubs) # empty list
library.return_pub(professor1, book1)
library.lend_pub(student1, book1) # the book should be available now
library.lend_pub(student1, journal2)
print(student1.pubs)
library.lend_pub(student2, journal1) # User not registred
