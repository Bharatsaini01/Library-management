
import controler
import models

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
    print("Enter 8 For Books_list")

def library_entrance(choose_no):
    if choose_no == 1:
        login()
    elif choose_no == 2:
        add_user()
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
    elif choose_no == 2:
        add_user()
    elif choose_no == 3:
        add_book()
    elif choose_no == 4:
        update_user_details()
    elif choose_no == 5:
        update_book_details()
    elif choose_no == 6:
        delete_user()
    else:
        print("!invalid no..")

def add_librarian():
    name = input("Enter Librarian Name : ")
    username = input("Create Librarian Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    controler.check_librarian(data)

def add_user():
    name = input("Enter User Name : ")
    username = input("Create User Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    controler.check_user(data)

def add_book():
    author = input("Enter Author Name : ")
    book_name = input("Enter Book Name : ")
    publication_company = input("Enter Publication Company : ")
    data = (author,book_name,publication_company)
    controler.check_book(data)

def update_user_details():
    username = input("Enter current username : ")
    new_name = input("Enter New Name : ")
    new_username = input("Enter New Username : ")
    new_password = input("Create New Password : ")
    new_mobile_no = input("Enter New Mobile no. : ")
    data = (new_name,new_username,new_password,new_mobile_no,username)
    if models.update_user_details(data):
        print("User Update successfully")
    else:
        print("username Already exists")

def update_book_details():
    book_name = input("Enter Book Name : ")
    new_author = input("Enter New Author Name : ")
    new_book_name = input("Enter New Book Name : ")
    new_publication_company = input("Enter New Publication Company : ")
    data = (new_author,new_book_name,new_publication_company,book_name)
    if models.update_book_details(data):
        print("Book Update successfully")
    else:
        print("Book Already exists")

def delete_user():
    username = input("Enter Username For Delete User : ")
    if models.delete_user(username):
        print("User Delete Successfully")
    else:
        print("!Incorrect Username")

def login():
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    if controler.admin_authotication(username,password):
        print("WELCOME LIBRARY MANAGEMENT SYSTEM")
        admin_functions_key()
        choose_no = int(input("choose any no. : "))
        admin_functions(choose_no)
    elif models.librarian_validation(username,password):
        print("WELCOME LIBRARY")
        librarian_functions_key()
        choose_no = int(input("choose any no. : "))
        librarian_functions(choose_no)
    elif models.user_validation(username,password):
        print("WELCOME LIBRARY")
        
        
    else:
        print("Incorrect Username or Password")
        
def home():
    print("Library Management System")
    library_entrance_key()
    choose_no = int(input("choose any no. : "))
    library_entrance(choose_no)

home()