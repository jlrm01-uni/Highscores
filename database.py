import logging

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

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


class Database:
    def __init__(self):
        self.session = Session()

    def get_all_highscores(self):
        return self.session.query(Highscores).all()

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

    def add_highscore(self, username, score):
        new_highscore = Highscores(username=username, score=score)

        pass

    def create_db(self):
        Base.metadata.create_all(engine)

        logging.info("Database created!")


if __name__ == '__main__':
    d = Database()

    d.reset_database()
    print(d.get_all_highscores())

    pass
