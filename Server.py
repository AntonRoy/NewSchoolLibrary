from flask import*

import os


app = Flask(__name__)

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
        if request.form['login'] == username and request.form['password'] == password:
            session['logged_in'] = True
            return redirect(url_for('main'))
        else:
            error = "Invalid username/password"
    return render_template('login.html', error=error)


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        select = request.form['select']
        print(select)
        if select == 'По ученику':
            stname = request.form['search']
            books = [['121123', 'dfdasf', 'dsfasads']]
            if len(books) >= 1:
                uch = True
            else:
                uch = 3
            return render_template('main.html', stname=stname, arrays=books, uch=uch)
        elif select == 'По книге':
            stname = request.form['search']
            students = [['121123', 'dfdasf', 'dsfasads']]
            if len(students) >= 1:
                uch = False
            else:
                uch = 3
            return render_template('main.html', stname=stname, arrays=students, uch=uch)

    return render_template('main.html', stname=None, arrays=None, klass=None, uch=None)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('start'))


@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':
        name = request.form['book']
        author = request.form['author']
        in_Stock = request.form['inlib']
        All_Books = request.form['all']
        print(name, author, in_Stock, All_Books)
        return render_template('OK.html')
    return render_template('add book.html', all_returned=' ')

app.secret_key = os.urandom(24)


if __name__ == '__main__':
    app.run(debug=True)
