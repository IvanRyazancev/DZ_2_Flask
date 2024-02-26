# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
# cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет
# отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    user_name = request.form['name']
    user_email = request.form['email']
    response = make_response(redirect(url_for('greet')))
    response.set_cookie('user_name', user_name)
    response.set_cookie('user_email', user_email)
    return response

@app.route('/greet')
def greet():
    user_name = request.cookies.get('user_name')
    return render_template('greet.html', user_name=user_name)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_name', '', expires=0)
    response.set_cookie('user_email', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)