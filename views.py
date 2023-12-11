
import controler
import models
import datetime

def library_entrance_key():
    print("Enter 1 For Login")
    print("Enter 2 For Register")

def admin_functions_key():
    print("Enter 1 For Add Librarian")
    print("Enter 2 For Add User")
    print("Enter 3 For Add Book")

def librarian_functions_key():
    print("Enter 1 For Add Librarian")
    print("Enter 2 For Add User")
    print("Enter 3 For Add Book")
    print("Enter 4 For Update User Details")
    print("Enter 5 For Update Book details")
    print("Enter 6 For Delete User")
    print("Enter 7 For delete Book")
    print("Enter 8 For Books list")
    print("Enter Othey key For Exit")


def user_functions_key():
    print("Enter 1 For Rent A Book")
    print("Enter 2 For Rent Out A Book")
    print("Enter 3 For Rented Books")
    print("Enter Other Key For Exit")
   
def user_functions(choose_no,username):
    if choose_no == 1:
        rent_book(username)
        user_home(username)
    elif choose_no == 2:
        rent_out_book()
        user_home(username)
    elif choose_no == 3:
        controler.rented_books(username)
        user_home(username)
    else:
        print("!invalid no..")

def library_entrance(choose_no):
    if choose_no == 1:
        login()
    elif choose_no == 2:
        add_user()
        entrance_home()
    else:
        print("!invalid no..")
        home()

def admin_functions(choose_no):
    if choose_no == 1:
        add_librarian()
    elif choose_no == 2:
        add_user()
    elif choose_no == 3:
        add_book()
    else:
        print("!invalid no..")

def librarian_functions(choose_no):
    if choose_no == 1:
        add_librarian()
        librarian_home()
    elif choose_no == 2:
        add_user()
        librarian_home()
    elif choose_no == 3:
        add_book()
        librarian_home()
    elif choose_no == 4:
        update_user_details()
        librarian_home()
    elif choose_no == 5:
        update_book_details()
        librarian_home()
    elif choose_no == 6:
        delete_user()
        librarian_home()
    elif choose_no == 7:
        delete_book()
        librarian_home()
    elif choose_no == 8:
        controler.book_list()
        librarian_home()
    else:
        print("!invalid no..")

def add_librarian():
    name = input("Enter Librarian Name : ")
    username = input("Create Librarian Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    controler.check_librarian(data,username)

def add_user():
    name = input("Enter User Name : ")
    username = input("Create User Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    controler.check_user(data,username)

def add_book():
    author = input("Enter Author Name : ")
    book_name = input("Enter Book Name : ")
    publication_company = input("Enter Publication Company : ")
    data = (author,book_name,publication_company)
    controler.check_book(data,book_name)

def update_user_details():
    username = input("Enter current username : ")
    new_name = input("Enter New Name : ")
    new_username = input("Enter New Username : ")
    new_password = input("Create New Password : ")
    new_mobile_no = input("Enter New Mobile no. : ")
    data = (new_name,new_username,new_password,new_mobile_no,username)
    if controler.update_user_details(data,username):
        print("User Update successfully")
    

def update_book_details():
    book_name = input("Enter Book Name : ")
    new_author = input("Enter New Author Name : ")
    new_book_name = input("Enter New Book Name : ")
    new_publication_company = input("Enter New Publication Company : ")
    data = (new_author,new_book_name,new_publication_company,book_name)
    if controler.update_book_details(data,book_name):
        print("Book Update successfully")
    

def delete_user():
    username = input("Enter Username For Delete User : ")
    if controler.delete_user(username):
        print("User Delete Successfully")
    else:
        print("Username Already not exists")

def delete_book():
    book_name = input("Enter Book Name For Delete Book : ")
    if models.delete_book(book_name):
        print("Book Delete Successfully")
    else:
        print("Book Name Already not exists")

def rent_book(username):
    controler.book_list()
    rent_book_name = input("Enter Book name for rent a Book : ")
    rented_date = datetime.datetime.now().date()
    data = (rented_date,username,rent_book_name)
    controler.rent_book(data,rent_book_name)

def rent_out_book():
    rent_out_book_name = input("Enter Book Name for Rent Out : ")
    rent_out_date = datetime.datetime.now().date()
    controler.rent_out_book(rent_out_book_name)

def entrance_home():
    library_entrance_key()
    choose_no = int(input("choose any no. : "))
    library_entrance(choose_no)

def librarian_home():
    librarian_functions_key()
    choose_no = int(input("choose any no. : "))
    librarian_functions(choose_no)


def user_home(username):
    user_functions_key()
    choose_no = int(input("choose any no. : "))
    user_functions(choose_no,username)
    

def login():
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    current_date = datetime.datetime.now().date()
    current_date = datetime.date(2024,1,1)
    if controler.admin_authotication(username,password):
        print("WELCOME LIBRARY MANAGEMENT SYSTEM")
        admin_functions_key()
        choose_no = int(input("choose any no. : "))
        admin_functions(choose_no)
    elif models.librarian_validation(username,password):
        print("WELCOME LIBRARY")
        controler.librarian_notice(current_date)
        librarian_home()
    elif models.user_validation(username,password):
        print("WELCOME LIBRARY")
        controler.notice(username,current_date)
        user_home(username)
    else:
        print("Incorrect Username or Password")
        
def home():
    print("Library Management System")
    entrance_home()

home()