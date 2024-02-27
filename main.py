from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

# main page
@app.route('/')
def index():
    return render_template('index.html')


# button para sa login form
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('main_page'))
    else:
        return redirect(url_for('wrong_password'))


# wrong password
@app.route('/')
def wrong_password():
    return render_template('index.html', message='Invalid username or password')


# redirect sa main page kapag tama
@app.route('/main_page')
def main_page():
    return  # render_template('forgot-password.html') return dapat sa main page kaso wala pa


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


if __name__ == '__main__':
    app.run(debug=True)
