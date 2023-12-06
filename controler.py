
import models
import datetime

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

def rent_book(data,rent_book_name):
    rented_user = models.check_rented_user(rent_book_name)
    if rented_user:
        if rented_user[0] is None:
            if models.get_book(rent_book_name):
                models.rent_book(data)
                print("Rented Book Successfully")
            else:
                print("This Book Not Available")
        else:
            print("Book Already Rented")
    else:
        if models.get_book(rent_book_name):
            models.rent_book(data)
            print("Rented Book Successfully")
        else:
            print("This Book Not Available")


def rent_out_book(rent_out_book_name):
    if models.get_book(rent_out_book_name):
        rented_user = models.check_rented_user(rent_out_book_name)
        if rented_user:
            if rented_user[0] is None:
                print("This Book Not Rented")
            else:
                models.rent_out_book(rent_out_book_name)
                print("Book Successfully Rent Out")
        else:
            print("This Book Not Rented")
    else:
        print("This Book Not Available")

def update_user_details(data,username):
    if models.get_user(username):
        models.update_user_details(data)
        return True
    else:
        print("User Not Found")

def update_book_details(data,book_name):
    if models.get_book(book_name):
        models.update_book_details(data)
        return True
    else:
        print("Book Not Found")

def book_list():
    book_list = models.get_books_list()
    print("Available Books ")
    print("{}    {}    {}    {}    {}    ".format("Author","book name","publication company","ranted date","ranted user"))
    for i in book_list:
        print("{0[0]}    {0[1]}    {0[2]}    {0[3]}    {0[4]}    ".format(i))

def rented_books(username):
    book_list = models.rented_books(username)
    print("Rented Books ")
    print("{}    {}    {}    {}    {}    ".format("Author","book name","publication company","ranted date","ranted user"))
    for i in book_list:
        print("{0[0]}    {0[1]}    {0[2]}    {0[3]}    {0[4]}    ".format(i))



def count_fine(notice_days):
    fine_days = 20
    fine = 0
    extra_fine = 0
    for i in range(notice_days):
        if notice_days > fine_days:
            fine += 20 + extra_fine
            extra_fine += 5
            fine_days += 5
    return fine 

def notice(username,current_date):
    rented_data = models.get_rented_data(username)
    for i in rented_data:
        rented_date,book_name = i
        notice = current_date - datetime.datetime.strptime(rented_date,"%Y-%m-%d").date()
        if notice.days >= 14:
            fine = count_fine(notice.days)
            print("Your Rented Book {}  {} Days Completed And Fine is {}.".format(book_name,notice.days,fine))
            
def librarian_notice(current_date):
    books = models.get_books_list()
    for i in books:
        author,book_name,publication_company,rented_date,username = i
        if rented_date:
            notice = current_date - datetime.datetime.strptime(rented_date,"%Y-%m-%d").date()
            if notice.days >= 14:
                print("{} book was rented by {} and {} days completed".format(book_name,username,notice.days))




              



