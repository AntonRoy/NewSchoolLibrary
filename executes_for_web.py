import pypyodbc
from bs4 import BeautifulSoup
import urllib.request


def Add_Book(isbn, cnt):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=PC\TSL_AD;'
                                      'DATABASE=TSL;'
                                      'UID=sa;'
                                      'PWD=2718281828')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    book_meta = heh(isbn)
    if not book_meta[0]:
        connection.commit()
        connection.close()
        return False
    request1 = cursor.execute(("select * from Books_Tab where ISBN = '{0}'").format(isbn)).fetchall()
    if request1:
        request = cursor.execute(("update Books_Tab set In_Stock = In_Stock + '{1}' where ISBN = '{0}'").format(isbn, cnt).fetchall())
        connection.commit()
        connection.close()
        return True
    request2 = cursor.execute(("INSERT INTO Books_Tab (ISBN, Name_Of_Book, Author_Of_Book) VALUES ('{0}', '{1}', '{2}')").format(isbn, book_meta[1], book_meta[2])).fetchall()
    connection.commit()
    connection.close()
    return True

def Search_Of_Student(Name):
    print('Trying to connect:')
    try:
        connection = pypyodbc.connect('DRIVER={SQL Server};'
                                      'SERVER=PC\TSL_AD;'
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
                                      'SERVER=PC\TSL_AD;'
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
                                      'SERVER=PC\TSL_AD;'
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
                                      'SERVER=PC\TSL_AD;'
                                      'DATABASE=TSL;'
                                      'Trusted_connection=True')
        print('Connected')
    except:
        print('Could not connect')
    cursor = connection.cursor()
    request = cursor.execute(("select ID from Books_Tab where Name_Of_Book = '{0}' and Author_Of_Book = '{1}'").format(Name, Author)).fetchall()
    connection.close()
    return request[0][0]


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def heh(isb):
    html = get_html('http://www.bookfinder.com/search/?author=&title=&lang=en&isbn='+ str(isb) + '&new_used=*&destination=ru&currency=RUB&mode=basic&st=sr&ac=qr')
    soup = BeautifulSoup(html)
    book_name = soup.find('span', itemprop='name')
    book_author = soup.find('span', itemprop='author')
    try:
        book_name = str(book_name.prettify())
        book_name = book_name[book_name.find('>') + 1:book_name.find('</') - 1]
        book_author = str(book_author.prettify())
        book_author = book_author[book_author.find('>') + 1:book_author.find('>/') - 6]
        return (True, translit(book_name[2:]), author(translit(book_author[2:-1])))
    except:
        return (False, None)


def translit(s):
    i = 0
    s = s.lower()
    sf = ''
    dict = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'z': 'з', 'i': 'и', 'y': 'ы', 'k': 'к',
            'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
            'c': 'ц', 'h':'х'}
    while i < len(s) - 1:
        if s[i] == 'j':
            i += 1
            if s[i] == 'e':
                sf += 'ё'
            elif s[i] == 's':
                i += 1
                if s[i] == 'h':
                    sf += 'щ'
            elif s[i] == 'u':
                sf += 'ю'
            elif s[i] == 'h':
                sf += 'ь'
            elif s[i] == 'a':
                sf += 'я'
        elif s[i] == 'z' and s[i + 1] == 'h':
            i += 1
            sf += 'ж'
        elif s[i] == 'k' and s[i + 1] == 'h':
            i += 1
            sf += 'х'
        elif s[i] == 'c' and s[i + 1] == 'h':
            i += 1
            sf += 'ч'
        elif s[i] == 's' and s[i + 1] == 'h':
            i += 1
            sf += 'ш'
        elif s[i] == 'h' and s[i + 1] == 'h':
            i += 1
            sf += 'ъ'
        elif s[i] == 'i' and s[i + 1] == 'h':
            i += 1
            sf += 'ы'
        elif s[i] == 'e' and s[i + 1] == 'h':
            i += 1
            sf += 'э'
        else:
            if s[i] not in dict.keys():
                sf += s[i]
            else:
                sf += dict[s[i]]
        i += 1
    if len(s) != len(sf):
        if s[-1] not in dict.keys():
            sf += s[-1]
        else:
            sf += dict[s[-1]]
    s = list(sf)
    delit = False
    for i in range(len(s) - 1):
        if (s[i] == 'и' or s[i] == 'й') and s[i + 1] == 'а':
            s[i] = 'я'
            s[i + 1] = ''
        elif s[i] == 'и' and s[i + 1] == 'и':
            s[i+1] = 'й'
        elif s[i] == 'ы' and s[i + 1] == 'a':
            s [i] = ''
        elif s[i] == 'т' and s[i + 1] == 'ц':
            s[i] = ''
        elif s[i] == 'ы' and s[i + 1] == 'а':
            s[i] = 'я'
            s[i + 1] = ''
        elif s[i] == 'с' and s[i + 1] == 'ч':
            s[i] = 'щ'
            s[i + 1] = ''
        elif s[i] == 'т' and s[i + 1] == 'с':
            s[i] = 'ц'
            s[i + 1] = ''
        elif s[i] == 'е' and s[i + 1] == 'и':
            s[i + 1] = 'й'
        elif s[i] == 'и' and s[i + 1] == 'ы':
            s[i + 1] = 'й'
        elif s[i] == 'х' and s[i] == s[i + 1]:
            s[i] = ''
        elif s[i] == '.':
            s[i] = ''
        if s[i] == '[':
            delit = True
        if delit:
            s[i] = ''
        if s[i] == ']':
            delit = False
        if s[i] in set(list(',.;')):
            s[i] = ''
        elif s[i] in set(list('abcdefghijklmnopqrstuvwxyz')):
            s[i] = ''
    if s[-1] in set(list('-,.;')):
        s[-1] = ''
    if s[-1] in set(list('abcdefghijklmnopqrstuvwxyz')):
        s[-1] = ''
    s = list(''.join(s))
    if s[-2] == ' ' and s[-1] not in set(list('скуова')):
        s[-2] = ''
        s[-1] = ''
    s[0] = s[0].upper()
    return ''.join(s)


def author(auth):
    auth = auth.split()
    auth = list(map(lambda x: x[0].upper() + x[1:], auth))
    auth = list(map(lambda x: x[0] if len(x) == 2 else x, auth))
    return ' '.join(auth)