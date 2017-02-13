from flask import*
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)


username = 'a1'
password = 'a1'


@app.route('/')
def start():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('start.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print()
        if request.form['login'] == username and request.form['password'] == password:
            session['logged_in'] = True
            return redirect(url_for('main'))
        else:
            error = "Invalid username/password"
    return render_template('Login.html', error=error)


@app.route('/main', methods=['GET', 'POST'])
def main():
    stname = None
    if request.method == 'POST':
        try:
            change=request.form['Change']
            print(change, type(change), stname)
            uch = True
            return render_template('main.html', stname='Книга Удалена', arrays=None, uch=None, isdeleted='Удалено')
        except:
            select = request.form['select']
            print(select)
            if select == 'По ученику':
                stname = request.form['search']
                books = [['Windows 10', '12.12.2016', '22.01.2016']]
                if len(books) >= 1:
                    uch = True
                else:
                    uch = 3
                return render_template('main.html', stname=stname, arrays=books, uch=uch, isdeleted='')
            elif select == 'По книге':
                stname = request.form['search']
                students = [['Антон Ройтерштейн', '12.12.2016', '22.01.2016']]
                if len(students) >= 1:
                    uch = False
                else:
                    uch = 3
            return render_template('main.html', stname=stname, arrays=students, uch=uch, isdeleted='')

    return render_template('main.html', stname=None, arrays=None, klass=None, uch=None, isdeleted='')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('start'))


@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':
        skan = request.form['scan']
        print(skan)
        return render_template('add book.html', all_returned='Отправлено!')
    return render_template('add book.html', all_returned=' ')

app.secret_key = os.urandom(24)

@app.route('/changes')
def changes():

    return render_template('changes.html')

if __name__ == '__main__':
    app.run(debug=True)
