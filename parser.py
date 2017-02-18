from bs4 import BeautifulSoup
import urllib.request

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def author_and_name(isbn):
    html = get_html('http://www.bookfinder.com/search/?author=&title=&lang=en&isbn='+ str(isbn) + '&new_used=*&destination=ru&currency=RUB&mode=basic&st=sr&ac=qr')
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
        return (False)


def translit(s):
    i = 0
    s = s.lower()
    print(s)
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

print(author_and_name(input()))