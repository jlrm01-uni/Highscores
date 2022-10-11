from flask import Flask, render_template

from database import Database

app = Flask(__name__)

d = Database()


@app.route("/")
def main():
    scores = d.get_all_highscores()
    return render_template("index.html", a=10, name="Kelvin", scores=scores)


if __name__ == '__main__':
    app.run(debug=True)
