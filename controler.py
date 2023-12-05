
import models

def admin_authotication(username,password):
    if username == "admin" and password == "admin":
        return True
    return False


def check_librarian(data):
    if models.add_librarian(data):
        print("Librarian add successfully")
    else:
        print("This username already exists")

def check_user(data):
    if models.add_user(data):
        print("User add successfully")
    else:
        print("This username already exists")

def check_book(data):
    if models.add_book(data):
        print("Book add successfully")
    else:
        print("This book already exists")