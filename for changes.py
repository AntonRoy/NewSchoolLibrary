from flask import*
from flask_bootstrap import Bootstrap
import os
import executes_for_web

app = Flask(__name__)
bootstrap = Bootstrap(app)


username = 'a1'
password = 'a1'


@app.route('/')
def start():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('main'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print()
        if request.form['login'] == username and request.form['password'] == password:
            session['logged_in'] = True
            return redirect(url_for('main'))
        else:
            error = " Неверный логин/пароль"
    return render_template('Login.html', error=error)


@app.route('/main', methods=['GET', 'POST'])
def main():
    stname = None
    a_stud = 'active'
    a_book = ''
    div_stud = 'tab-pane active fade in'
    div_book = 'tab-pane fade in'
    if request.method == 'POST':
        try:
            selectedStud = request.form['stud']
            types = request.form['type']
            if types == 'True':
                uch = True
                data = executes_for_web.Search_Of_Student(selectedStud)
            else:
                a_stud = ''
                a_book = 'active'
                div_stud = 'tab-pane fade in'
                div_book = 'tab-pane active fade in'
                uch = False
                selectedStud.split(', ')
                data = executes_for_web.Search_Of_Book(selectedStud[1],selectedStud[0])
            print(selectedStud, types)
            return render_template('found.html', stname=selectedStud, arrays=data, uch=uch)
        except:
            select = request.form["select"]
            print(select)
            if select == 'По ученику':
                name = request.form['name']
                surname = request.form['surname']
                grade = request.form['numclass'] + request.form['letterclass']
                try:
                    gender = request.form['gender']
                except:
                    gender = ''
                #print(name, surname, gender, grade)
                books=[['Windows 10', '12.12.2016', '22.01.2016']]
                puple=[ "Антон Мазур", "Максим Мазур"]
                if grade == "--":
                    grade = ''
                else:
                    grade = 'Класс: ' + grade
                if len(puple) > 1:
                    uch = True
                elif len(puple) == 1:
                    return render_template('found.html', stname=name + ' ' + surname, klass=grade, arrays=books)
                else:
                    uch = 140
                return render_template('newmain.html', stname=name + ' ' + surname, klass=grade, arrays=puple, uch=uch,
                                       a_book=a_book, a_stud=a_stud, div_book=div_book, div_stud=div_stud)

            elif select == 'По книге':
                a_stud = ''
                a_book = 'active'
                div_stud = 'tab-pane fade in'
                div_book = 'tab-pane active fade in'
                title = request.form['title']
                author = request.form['surname']
                stname = title + ', ' + author
                students = ['Достоевский, Преступление и наказание', "Ницше, Так говорил Заратустра", "Данте, Божественная Комедия"]
                data = [
                    ['Антон Ройтерштейн', "20.01.2017", '20.02.2017'],
                    ['Денис Мазур', "1.02.2017", '1.03.2017']
                        ]
                if len(students) > 1:
                    uch = False
                    return render_template('newmain.html', stname=stname, arrays=students, uch=uch,
                                           a_book=a_book, a_stud=a_stud, div_book=div_book, div_stud=div_stud)
                elif len(students) == 1:
                    uch = False
                    print(stname, data)
                    return render_template('found.html', stname=stname, arrays=data, uch=uch)
                if len(stname) <= 2:
                    stname = "Имя не указано"
                    return render_template('newmain.html', stname=stname, arrays=None, uch=None,
                    a_book=a_book, a_stud=a_stud, div_book=div_book, div_stud=div_stud)

    return render_template('newmain.html', stname=None, arrays=None, uch=None,
                           a_book=a_book, a_stud=a_stud, div_book=div_book, div_stud=div_stud)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('start'))


@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':
        code = request.form['scan']
        cnt = request.form['col']
        print(code, cnt)
        try:
            print(int(code))
        except:
            return render_template('add book.html', all_returned='', problem='ISBN должен состоять только из цифр')
        if len(code) < 13 or len(code) > 13:
            return render_template('add book.html', all_returned='', problem='ISBN должен состоять из 13 цифр')
        elif len(cnt) < 1 or int(cnt) < 1:
            return render_template('add book.html', all_returned='', problem='Количество книг не может быть меньше 1')
        else:
            add = executes_for_web.Add_Book(code, cnt)
            if add:
                return render_template('add book.html', all_returned='Добавлено!', problem='')
            else:
                return render_template('add book.html', all_returned='',
                                       problem='Такой книги в общей базе данных нет')

    return render_template('add book.html', all_returned='', problem='')

app.secret_key = os.urandom(24)


if __name__ == '__main__':
    app.run(debug=True)
