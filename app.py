from flask import Flask, render_template

from database import Database

app = Flask(__name__)


@app.route("/")
def main():
    return "hello world"


if __name__ == '__main__':
    app.run()