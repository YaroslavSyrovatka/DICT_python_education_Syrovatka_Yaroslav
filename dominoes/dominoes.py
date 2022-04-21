import random


class Dominoes:
    def __init__(self):
        self.all_bone = [[z, x] for z in range(7) for x in range(z, 7)]
        self.stok_domino = []
        self.player = []
        self.computer = []
        self.snake = []
        self.status = None


    def random_domino(self):
        """тут домно разделяются рандомно"""
        a = random.sample(self.all_bone, 28)
        self.player = a[0:7]
        self.computer = a[7:14]
        self.stok_domino = a[14:28]



    def menu(self):
        self.random_domino()
        self.first_step()
        self.chang_status()



domino = Dominoes()
domino.menu()