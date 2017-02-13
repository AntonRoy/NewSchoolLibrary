import pypyodbc

def Book_In_Library(Name_Of_Book1, Author_Of_Book1):
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
    request = cursor.execute(("select *from Books_Tab where Name_Of_Book = '{0}' and Author_Of_Book = '{1}' and Books_Tab.In_Stock > 0").format(Name_Of_Book1, Author_Of_Book1)).fetchall()
    connection.close()
    if len(request):
        return True
    return False


def Books_Of_Author_In_Library(Author):
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
    request = cursor.execute("select Name_Of_Book, In_Stock from Books_Tab where Author_Of_Book = '{0}'".format(Author)).fetchall()
    connection.close()
    if request:
        return request
    return 'Извините, но книги данного автора не найдены'


def list_of_debts(ID_In_Database):
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
    request = cursor.execute("select Book from Books_Of_Student where Student = '{0}'".format(ID_In_Database[0][0])).fetchall()
    debts = set()
    for debt in request:
        debtt = cursor.execute("select Type_Of_Book from Book_Tab where ID = {0}".format(debt[0])).fetchall()
        debtf = cursor.execute("select Name_Of_Book, Author_Of_Book from Main_Books_Tab where ID = {0}".format(debtt[0][0])).fetchall()
        debts.add(debtf[0])
    return list(debts)
    connection.close()


def ID_Of_Name(ID_Vk):
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
    request = cursor.execute("select ID from Main_Tab where ID_Vk = '{0}'".format(ID_Vk)).fetchall()
    connection.close()
    return request


def Book_Of_Id(ID):
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
    request = cursor.execute("select Name_Of_Book, Author_Of_Book from Main_Books_Tab where ID = '{0}'".format(ID)).fetchall()
    connection.close()
    return request