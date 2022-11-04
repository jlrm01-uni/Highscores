from flask import Flask, render_template
from livereload import Server
from database import Database

app = Flask(__name__)

d = Database()


@app.route("/")
def main():

    return render_template("index.html", a=10, name="Kelvin")


@app.route("/reset_database")
def reset_database():
    d.reset_database()
    return "Everything's gone, chief!"


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/highscores")
def highscores():
    scores = d.get_all_highscores()
    return render_template("highscores.html", scores=scores)


if __name__ == '__main__':
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()

    # app.run(debug=True)
