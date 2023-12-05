
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
    check = cursor.execute("UPDATE USERS SET (NAME,USERNAME,PASSWORD,MOBILE_NO) = (?,?,?,?) WHERE USERNAME = (?)",data)
    connection.commit()
    if check:
        return True
    return False

def update_book_details(data):
    check = cursor.execute("UPDATE BOOKS SET (AUTHOR,BOOK_NAME,PUBLICATION_COMPANY) = (?,?,?) WHERE BOOK_NAME = (?)",data)
    connection.commit()
    if check:
        return True
    return False

def delete_user(username):
    check = cursor.execute("DELETE USERS WHERE USERNAME = (?)",username)
    connection.commit()
    if check:
        return True
    return False

def delete_book(book_name):
    check = cursor.execute("DELETE BOOKS WHERE BOOK_NAME = (?)",book_name)
    connection.commit()
    if check:
        return True
    return False

connection.commit()
