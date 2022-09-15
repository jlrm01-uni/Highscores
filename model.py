class Model:
    def __init__(self):
        self.highscores = []

    def add_highscore(self, username, score):
        self.highscores.append((username, score))

    def delete_highscore_by_index(self, index):
        del self.highscores[index]


if __name__ == '__main__':
    m = Model()

    m.add_highscore("Victor", 0)
    m.add_highscore("Juan", 1000000)
    m.add_highscore("Jorge", 1000001)

    m.delete_highscore_by_index(-1)

    print(m.highscores)

    pass
