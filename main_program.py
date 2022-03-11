from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Анкета', form=form, photo=url_for('static', filename='img/mission_small.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
