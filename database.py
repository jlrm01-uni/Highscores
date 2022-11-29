import logging
import arrow
from sqlalchemy import create_engine, Column, Integer, String, desc, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os

HIGHSCORES_LIMIT = 10
NEWS_LIMIT = 5

connection_string = os.getenv("POSTGRES_URL")

engine = create_engine(connection_string)
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)


class Highscores(Base):
    __tablename__ = "highscores"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    score = Column(Integer)

    def __repr__(self):
        return f"{self.username}: {self.score}"


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    date_created = Column(DateTime)

    def __repr__(self):
        return f"{self.title}: {self.content[:20]}"


class Database:
    def __init__(self):
        self.session = Session()

    def get_all_highscores(self):
        return self.session.query(Highscores).order_by(desc(Highscores.score)).limit(HIGHSCORES_LIMIT).all()

    def get_all_news(self):
        return self.session.query(News).limit(NEWS_LIMIT).all()

    def add_test_highscores(self):
        new = Highscores(username="Juan", score=1000)
        other = Highscores(username="Kelvin", score=20)

        self.session.add(new)
        self.session.add(other)

        rest_of_them = [
            Highscores(username="Mimi", score=10001),
            Highscores(username="Harry", score=1001),
            Highscores(username="Mary", score=10001),
            Highscores(username="Luna", score=301),
            Highscores(username="Relm", score=101),
            Highscores(username="Stragos", score=11),
            Highscores(username="Sabin", score=100001),
        ]

        self.session.add_all(rest_of_them)
        self.session.commit()

    def nuke_database(self):
        Base.metadata.drop_all(engine)

    def reset_database(self):
        self.nuke_database()
        self.create_db()
        self.add_test_highscores()
        self.add_test_news()

    def add_highscore(self, username, score):
        new_highscore = Highscores(username=username, score=score)

        pass

    def create_db(self):
        Base.metadata.create_all(engine)

        logging.info("Database created!")

    def add_test_news(self):
        now = arrow.utcnow().datetime

        test_news = News(title="Greatest News Ever",
                         content="Kelvin gets platinum in God of War",
                         date_created=now)

        self.session.add(test_news)
        self.session.commit()

    def add_new_news(self, title, content, date):
        new_news = News(title=title, content=content, date_created=date)

        self.session.add(new_news)
        self.session.commit()


if __name__ == '__main__':
    d = Database()

    d.reset_database()
    print(d.get_all_highscores())

    pass
