import pickle


class Npc:
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name

with open('npc.pickle', 'rb') as f:
    group = pickle.load(f)


for m in group:
    print(type(m))
    print(m.name, m.x, m.y)