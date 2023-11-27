import pickle

class Npc:
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name


yuri = Npc('yuri', 100, 200)
zeni = Npc('jeni', 200, 400)
group = [yuri, zeni]

with open('npc.pickle', 'wb') as f:
    pickle.dump(group, f)