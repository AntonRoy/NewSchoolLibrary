import pypyodbc

def Add_Type_Of_Book(In_Stock, All_Books, Name_Of_Book, Author_Of_Book):
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
    request = cursor.execute(("INSERT INTO Main_Books_Tab (In_Stock, All_Books, Name_Of_Book, Author_Of_Book) VALUES ('{0}', '{1}', '{2}', '{3}')").format(In_Stock, All_Books, Name_Of_Book, Author_Of_Book)).fetchall()
    connection.commit()
    connection.close()


def Add_Book(Type_Of_Book, ID_Book):
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
    request = cursor.execute(("INSERT INTO Book_Tab (Type_Of_Book, ID_Books) VALUES ('{0}', '{1}')").format(Type_Of_Book, ID_Book)).fetchall()
    connection.commit()
    connection.close()

def Search_Of_Student(Name):
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
    request = cursor.execute(("SELECT Book, Data_Of_Receipt, Date_Of_Return FROM Books_Of_Student WHERE Student = '{0}'").format(Name)).fetchall()
    connection.close()
    return request



def Search_Of_Book(Book):
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
    request = cursor.execute(("SELECT Student FROM Books_Of_Student WHERE Book = '{0}'").format(Book)).fetchall()
    connection.close()
    return request[0][0]