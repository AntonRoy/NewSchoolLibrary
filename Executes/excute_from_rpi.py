import pypyodbc
import datetime
import send_message

def Book_of_ID(BookID):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=DESKTOP-T62E4DK\SQLEXPRESS;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    request = cursor.execute(("SELECT ID FROM Book_Tab where ID_Book = '{0}'").format(BookID)).fetchall()
    connection.close()
    return request[0]


def take_book(Student, Book):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=DESKTOP-T62E4DK\SQLEXPRESS;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    request = cursor.execute(("INSERT INTO Main_Books_Tab (Student, Book, Date_Of_Receipt) VALUES ('{0}', '{1}', '{2}')").format(Student, Book, datetime.datetime.now())).fetchall()
    connection.commit()
    send_message.send_smth(Student, ("Вы успешно взяли книгу '{0}'").format(Book))
    connection.close()


def return_book(Student, Book):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=DESKTOP-T62E4DK\SQLEXPRESS;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    request = cursor.execute(("DELETE FROM Main_Books_Tab (Student, Book, Date_Of_Receipt) VALUES ('{0}', '{1}', '{2}')").format(Student, Book, datetime.datetime.now())).fetchall()
    send_message.send_smth(Student, ("Вы успешно сдали книгу '{0}'").format(Book))

    connection.close()