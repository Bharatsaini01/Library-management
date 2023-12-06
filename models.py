
import sqlite3

connection = sqlite3.connect('library management.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS USERS
               (
                NAME TEXT NOT NULL,
                USERNAME TEXT NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL,
                MOBILE_NO INT NOT NULL 
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS LIBRARIAN
               (
                NAME TEXT NOT NULL,
                USERNAME TEXT NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL,
                MOBILE_NO INT NOT NULL              
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS BOOKS
               (
                AUTHOR TEXT NOT NULL,
                BOOK_NAME TEXT NOT NULL UNIQUE,
                PUBLICATION_COMPANY TEXT NOT NULL,
                RENTED_DATE DATE,
                RENTED_USER TEXT               
               )""")

def librarian_validation(username,password):
    cursor.execute("SELECT PASSWORD FROM LIBRARIAN WHERE USERNAME = (?)",(username,))
    Password = cursor.fetchone()
    if Password:
        if password in Password:
            return True
        return False
    return False

librarian_validation("surya","surya123")
def user_validation(username,password):
    cursor.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = (?)",(username,))
    Password = cursor.fetchone()
    if Password:
        if password in Password:
            return True
        return False
    return False

def add_librarian(data):
    check = cursor.execute("INSERT INTO LIBRARIAN VALUES(?,?,?,?)",data)
    connection.commit()
    if check:
        return True
    return False

def add_user(data):
    check = cursor.execute("INSERT INTO USERS VALUES(?,?,?,?)",data)
    connection.commit()
    if check:
        return True
    return False

def add_book(data):
    check = cursor.execute("INSERT INTO BOOKS (AUTHOR,BOOK_NAME,PUBLICATION_COMPANY) VALUES(?,?,?)",data)
    connection.commit()
    if check:
        return True
        connection.close()
    return False

def update_user_details(data):
    cursor.execute("UPDATE USERS SET (NAME,USERNAME,PASSWORD,MOBILE_NO) = (?,?,?,?) WHERE USERNAME = (?)",data)
    connection.commit()
    

def update_book_details(data):
    cursor.execute("UPDATE BOOKS SET (AUTHOR,BOOK_NAME,PUBLICATION_COMPANY) = (?,?,?) WHERE BOOK_NAME = (?)",data)
    connection.commit()
    

def get_user(username):
    cursor.execute("SELECT * FROM USERS WHERE USERNAME=(?)",(username,))
    check = cursor.fetchone()
    return check

def get_book(book_name):
    cursor.execute("SELECT * FROM BOOKS WHERE BOOK_NAME=(?)",(book_name,))
    check = cursor.fetchone()
    return check

def check_rented_user(book_name):
    cursor.execute("SELECT RENTED_USER FROM BOOKS WHERE BOOK_NAME=(?)",(book_name,))
    check = cursor.fetchone()
    return check


def get_books_list():
    cursor.execute("SELECT * FROM BOOKS")
    book_list = cursor.fetchall()
    return book_list

def delete_user(username):
    if get_user(username):
        cursor.execute("DELETE FROM USERS WHERE USERNAME = (?)",(username,))
        connection.commit()
        return True
    return False
        

def delete_book(book_name):
    if get_book(book_name):
        cursor.execute("DELETE FROM BOOKS WHERE BOOK_NAME = (?)",(book_name,))
        connection.commit()
        return True
    return False

def rent_book(data):
    cursor.execute("UPDATE BOOKS SET (RENTED_DATE,RENTED_USER) = (?,?) WHERE BOOK_NAME = (?)", data)
    connection.commit()

def rent_out_book(rent_out_book_name):
    cursor.execute("UPDATE BOOKS SET (RENTED_DATE,RENTED_USER) = (NULL,NULL) WHERE BOOK_NAME = (?)",(rent_out_book_name,))
    connection.commit()

def rented_books(username):
    cursor.execute("SELECT * FROM BOOKS WHERE RENTED_USER = (?)",(username,))
    data = cursor.fetchall()
    return data

def get_rented_data(username):
    cursor.execute("SELECT RENTED_DATE,BOOK_NAME FROM BOOKS WHERE RENTED_USER=(?)",(username,))
    check = cursor.fetchall()
    return check




connection.commit()
