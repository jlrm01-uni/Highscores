from flask import Flask, render_template
from livereload import Server
from database import Database

app = Flask(__name__)

d = Database()


@app.route("/")
def main():
    scores = d.get_all_highscores()
    return render_template("index.html", a=10, name="Kelvin", scores=scores)


@app.route("/reset_database")
def reset_database():
    d.reset_database()
    return "Everything's gone, chief!"


if __name__ == '__main__':
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()

    # app.run(debug=True)
