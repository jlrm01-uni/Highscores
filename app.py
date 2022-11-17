from flask import Flask, render_template, request
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
    news = d.get_all_news()
    return render_template("news.html", news=news)


@app.route("/new_news")
def new_news():
    return render_template("new_news.html")


@app.route("/highscores")
def highscores():
    scores = d.get_all_highscores()
    return render_template("highscores.html", scores=scores)


@app.route("/highscores_json")
def highscores_json():
    scores = d.get_all_highscores()

    all_highscores = []

    for each_score in scores:
        user_score = each_score.score
        username = each_score.username

        all_highscores.append((username, user_score))

    return dict(highscores=all_highscores)


@app.route("/post_news", methods=["POST"])
def post_news():
    return "News created!"


if __name__ == '__main__':
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()

    # app.run(debug=True)
