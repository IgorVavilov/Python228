
import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDateBase import FDateBase

# конфигурация
DATABASE = "/tmp/flsk_dz_1.db"
DEBUG = True
SECRET_KEY = '1f028782a42d4d4f028ca16225a6767f3bc48d1b'


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk_dz_1.db'))

menu = [{"name": "Главная", "url": "index"},
        {"name": "Каталог", "url": "catalog"},
        {"name": "Техподдержка", "url": "support"},
        {"name": "Доставка, Оплата", "url": "delivery"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/catalog")
def catalog():
    db = get_db()
    dbase = FDateBase(db)
    # print(url_for('catalog'))
    return render_template("catalog.html", title="Каталог", menu=dbase.get_menu())


@app.route("/support")
def support():
    db = get_db()
    dbase = FDateBase(db)
    # print(url_for('support'))
    return render_template("support.html", title="Техподдержка", menu=dbase.get_menu())


@app.route("/delivery")
def delivery():
    db = get_db()
    dbase = FDateBase(db)
    # print(url_for('delivery'))
    return render_template("delivery.html", title="Доставка, Оплата", menu=dbase.get_menu())


@app.route("/contact", methods=["POST", "GET"])
def contact():
    db = get_db()
    dbase = FDateBase(db)
    if request.method == 'POST':
        # print(request.form)
        context = {
            "username": request.form['username'],
            "email": request.form['email'],
            "message": request.form['message'],
        }
        return render_template("contact.html", **context, title="Обратная связь", menu=dbase.get_menu())
    return render_template("contact.html", title="Обратная связь", menu=dbase.get_menu())


@app.route("/profile/<username>")
def profile(username):
    # if 'userLogged' not in session or session['userLogged'] != username:
    #     abort(401)
    return f"Пользователь: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    db = get_db()
    dbase = FDateBase(db)
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == 'igor' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDateBase(db)
    return render_template("page404.html", title='Страница не найдена', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
