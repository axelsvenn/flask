from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template("index.html", list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
