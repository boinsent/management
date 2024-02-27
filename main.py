from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="management"
)


# main page
@app.route('/')
def index():
    return render_template('index.html')


# button para sa login form
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = database.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
    account = cursor.fetchone()

    if account:
        return redirect(url_for('main_page'))
    else:
        return redirect(url_for('wrong_password'))


# wrong password
@app.route('/')
def wrong_password():
    return 'Wrong password'


# redirect sa main page kapag tama
@app.route('/main_page')
def main_page():
    return render_template('forgot-password.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


if __name__ == '__main__':
    app.run(debug=True)
