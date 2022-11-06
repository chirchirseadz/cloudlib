import os 

import datetime
"""

This is a library management system 

"""
class LMS:

    # This function initialize all the requirements of the Library 
    def __init__(self, list_of_books, library_name):

        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict =  {}
        Id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            # here we are updating our dictionary with the available books
            self.books_dict.update({
                str(Id): { 
                    'books_title': line.replace("\n",''),
                    'lender_name': "",
                    'issue_date': "",
                    'status': 'Available'

                    }
            })
            Id = Id + 1
    
    #  Display books module

    def display_books(self):

        print('---------------------------------- List of Books ---------------------------------')
        print("Books ID","\t", "Books Title" "\t\t\t" "Status")
        print('----------------------------------------------------------------------------------')

        for key, value in self.books_dict.items():

            print(f"{key} \t\t {value.get('books_title')} \t\t  {value.get('status')}" )


    # Isssue Books modeule  

    def issue_books(self):
        book_id = input("Enter Book Id: ")
        current_date  = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]['status'] == "Available":
                print(f"This book is already issued to {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['issue_date']}")
                return self.issue_books
            elif self.books_dict[book_id]['status'] == "Available":
                your_name = input("Enter name: ")
                self.books_dict[book_id]['lender_name'] = your_name
                self.books_dict[book_id]['issue_date'] = current_date
                self.books_dict[book_id]['status'] = "Already taken !!!"
                print("Book Issued Successfully !!! \n")
                

        else:
            print("The Book Id is not available !!! \n")
            return self.issue_books


    #  Add books module
    def add_books(self):
        new_books = input("Enter Title of the book: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title is too long !!! Length should be 20 characters long")

        else:
             with open(self.list_of_books) as bk:
                bk.writelines(f'{new_books} \n')

                self.books_dict.update(
                    {str(int(max(self.books_dict))+1):{"books_title": new_books, "lender_name": "","issue_date": "","status": "Available", }})
             
                print(f"This book {new_books} has been added successfully !!! ")


    # This is the Return Books module 

    def return_books(self):
        book_id = input("Enter book Id: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['status'] == "Available":
                print("The book with this Id Already exists !!!! ")
            elif not self.books_dict[book_id]['status'] == "Available":
                self.books_dict[book_id]['lender_name'] = ""
                self.books_dict[book_id]['issue_date']  = ""
                self.books_dict[book_id]['status'] = "Available"
                print("Successfully updated !!!!  \n")
        else:
            print("Books ID not found !!! ")




try:
    myLMS = LMS('list_of books.txt', 'Sydney Library')

    press_key_list = {
        'D': "Display Books",
        'I': 'Issue Books',
        'A': 'Add Books',
        'R': 'Return Books',
        'Q': 'Quit',
    }
    key_press = False

    while not (key_press == "q"):
        print(f"------------------Welcome To {myLMS.library_name} Management System-------------------------------\n")

        for key, values in press_key_list.items():
            print("Press",key, "To", values)
        key_press = input("Press Key: ").lower()
        if key_press == 'i':
            print('\nCurrent Session: Issue Books')
            myLMS.issue_books()
        elif key_press == 'd':
            print('\nCurrent Session: Display Books')
            myLMS.display_books()
        elif key_press == 'a':
            print('\nCurrrent Session: Add Books')
            myLMS.add_books()

        elif key_press == 'r':
            print('\nCurrent Session: Return Books')
            myLMS.return_books()
        elif key_press == 'q':
            break
        else:
            continue


except Exception as e:
    print("Something Went Wrong. Please Check your Input !!! ")







