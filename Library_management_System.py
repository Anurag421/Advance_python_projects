'''4. Library Management System
Problem Statement: Create a system that manages books, borrowers, and due dates.
Steps:
Design Book, Borrower, and Library classes with attributes like title, borrower ID, and due date.
Implement methods for lending, returning, and tracking books.
Handle overdue books with a fine-calculation method.'''


from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, book_id):

        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True
    
    def mark_as_borrowed(self):
        '''Set the book's status as borrowed'''
        self.is_available = False
    
    def mark_as_available(self):
        '''set the books status to available.'''
        self.is_available = True


class Borrower:
    def __init__(self, borrower_id, name):

        self.borrower_id = borrower_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        '''Record the borrowing of a book. '''
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        '''Remove the book from the list of borrowed books. '''
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):

        self.book_collection = {} #Dictionary to store books in the library
        self.borrowers = {} #Dictionary to store borrowers by borrowers_id
        self.due_date = {} #Dictionary to track the due dates by book_id
        self.fine_rate = 1 

    def add_book(self, title, author):
        '''Add a new book in the library collection.'''
        book_id = len(self.book_collection) + 1
        new_book = Book(title, author, book_id)
        self.book_collection[book_id] = new_book
        print(f"Book '{title}' by {author} added with id {book_id}.")

    def remove_book(self, book_id):
        '''Remove a book from  the collection usng its ID.'''
        if book_id in self.book_collection:
            removed_book = self.book_collection.pop(book_id)
            print(f"Book '{removed_book.title}' removed form the library.")
        else:
            print(f"Book with ID {book_id} does not exits.")

    def lend_book(self, book_id, borrower_id, due_date):
        '''Lend a book to a borrower and set the due date.'''
        if book_id in self.book_collection and self.book_collection[book_id].is_available:
            book = self.book_collection[book_id]
            borrower = self.borrowers[borrower_id]

            #lend the book
            book.mark_as_borrowed()
            borrower.borrow_book(book)
            self.due_date[book_id] = due_date

            print(f"Book '{book.title}' lent to {borrower.name}. Due date: {due_date}.")
        else:
            print(f"Borrwer with ID {borrower_id} does not exist.")

        print(f"Book with ID {book_id}  is not available or does not exits.")
        

    def retrun_book(self, book_id, borrower_id):
        '''Retrun a book to the library. '''
        if book_id in self.book_collection and borrower_id in self.borrowers:
            book = self.book_collection[book_id]
            borrower = self.borrowers[borrower_id]

            if book in borrower.borrowed_books:

                #Return the book
                book.mark_as_available()
                borrower.return_book(book)
                self.due_date.pop(book_id, None)

                print(f"Book '{book.title}' returned by {borrower.name}.")
            else:
                print(f"Book with ID '{book_id} was bot borrowed by {borrower.name}.")
        else:
            print('Invalid book or borrower ID.')
    
    def calculate_fine(self, book_id, current_date):
        '''Calculate overdue fine if the due date has passed.'''
        if book_id in self.due_date:
            due_date = datetime.strptime(self.due_dates[book_id], "%Y-%m-%d")
            current_date = datetime.strptime(current_date, "%Y-%m-%d")

            if current_date > due_date:
                #calculate the fine for the overdue days 
                overdue_days = (current_date - due_date).days
                fine = overdue_days * self.fine_rate
                print(f'Book with ID {book_id} is overdue by {overdue_days} days. ')
                return fine
            else:
                print(f'Books with ID {book_id} is not overdue.')
        else:
            print(f"No due date found for book ID {book_id}. ")
        return 0
    
    def add_borrwer(self, borrower_id, name):
        '''Add a new borrower to the library'''
        if borrower_id not in self.borrowers:
            new_borrowers = Borrower(borrower_id, name)
            self.borrowers[borrower_id] = new_borrowers
            print(f"Borrower '{name}' added with ID {borrower_id}.")
        else:
            print(f'Borrower with ID {borrower_id} already exits. ')

library = Library()
library.add_book('Python Programming', 'John Doe')
library.add_book('Machine Learning', 'Jane Smith')
library.add_borrwer(1, 'Alice')
library.add_borrwer(2, 'Bob')
library.lend_book(1,1, '2024-11-10')
library.retrun_book(1,1)
library.calculate_fine(1, '2024-11-15')










'''Steps to Implement:
Define Classes and Attributes:

Book Class: Manages individual book details.
Attributes: title, author, book_id, is_available.
Borrower Class: Manages the borrower’s information.
Attributes: borrower_id, name, borrowed_books (list of borrowed books).
Library Class: Manages the collection of books and operations.
Attributes: book_collection (list of all books), borrowers (list of all borrowers), due_dates (dictionary mapping book IDs to due dates), fine_rate.
Implement Core Methods:

Library Class Methods:

add_book(title, author): Add a new book to the library collection.
remove_book(book_id): Remove a book from the collection using its ID.
lend_book(book_id, borrower_id, due_date): Lend a book to a borrower and set the due date.
return_book(book_id, borrower_id): Return a book to the library.
calculate_fine(book_id, current_date): Calculate overdue fine if the due date has passed.
Borrower Class Methods:

borrow_book(book): Record the borrowing of a book.
return_book(book): Remove the book from the list of borrowed books.
Book Class Methods:

mark_as_borrowed(): Set the book’s status to unavailable.
mark_as_available(): Set the book’s status to available.
Handle Overdue Fines:

Implement the calculate_fine method in the Library class. Use attributes like due_date and fine_rate to determine the amount if a book is returned late'''