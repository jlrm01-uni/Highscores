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


class Database:
    def __init__(self):
        self.session = Session()

    def add_test_highscores(self):
        new = Highscores(username="Juan", score=1000)
        other = Highscores(username="Kelvin", score=20)

        d.session.add(new)
        d.session.add(other)

    def nuke_database(self):
        Base.metadata.drop_all(engine)

    def reset_database(self):
        self.nuke_database()
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

    pass
