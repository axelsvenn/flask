from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">для участия в миссии</h2>
                            <div>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label><br><br>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div><br>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        with open("static/img/photo.png", 'wb') as fd:
            f = request.files["file"]
            fd.write(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
