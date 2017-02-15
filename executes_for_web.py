import pypyodbc

def Add_Type_Of_Book(In_Stock, All_Books, Name_Of_Book, Author_Of_Book):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=PC\ANTON;'
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
                                      'SERVER=PC\ANTON;'
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
                                      'SERVER=PC\ANTON;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    id = ID_Of_Name(Name)
    cursor = connection.cursor()
    request = cursor.execute(("SELECT Book, Date_Of_Receipt, Date_Of_Return FROM Books_Of_Student WHERE Student = '{0}'").format(id)).fetchall()
    request = list(map(lambda x: list(x), request))
    for book in range(len(request)):
        book_name = cursor.execute(("SELECT Name_Of_Book FROM Books_Tab WHERE ID = '{0}'").format(request[book][0])).fetchall()
        print(book_name[0][0], request[book][0])
        request[book][0] = book_name[0][0]
    connection.close()
    return request



def Search_Of_Book(Book, Author):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=PC\ANTON;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    id = ID_Of_Book(Book, Author)
    request = cursor.execute(("select Student, Date_Of_Receipt, Date_Of_Return FROM Books_Of_Student WHERE Book = '{0}'").format(id)).fetchall()
    request = list(map(lambda x: list(x), request))
    for student in range(len(request)):
        student_name = cursor.execute(("SELECT First_Name, Last_Name FROM Main_Tab WHERE ID = '{0}'").format(request[student][0])).fetchall()
        request[student][0] = student_name[0][0] + ' ' + student_name[0][1]
    connection.close()
    return request

def ID_Of_Name(name):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=PC\ANTON;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    name = name.split()
    request = cursor.execute(("select ID from Main_Tab where First_Name = '{0}' and Last_Name = '{1}'").format(name[0], name[1])).fetchall()
    connection.close()
    return request[0][0]


def ID_Of_Book(Name, Author):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=PC\ANTON;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    request = cursor.execute(("select ID from Books_Tab where Name_Of_Book = '{0}' and Author_Of_Book = '{1}'").format(Name, Author)).fetchall()
    connection.close()
    return request[0][0]