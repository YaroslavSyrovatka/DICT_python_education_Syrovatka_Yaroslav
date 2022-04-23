import random


class Rock_paper_scissors:
    def __init__(self):
        self.pc = []
        self.resalt = 0
        self.name = str(input(f"Enter your name: >")).capitalize()
        self.simbols = {
            'rock': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            'paper': ['fire', 'scissors', 'wolf', 'tree', 'human', 'snake', 'sponge'],
            'scissors': ['gun', 'lightning', 'devil', 'dragon', 'water', 'rock', 'fire'],
            'gun': ['water', 'air', 'sponge', 'paper', 'devil', 'dragon'],
            'lightning': ['water', 'air', 'sponge', 'paper', 'dragon', 'wolf', 'lightning'],
            'devil': ['water', 'air', 'sponge', 'paper', 'tree', 'wolf', 'dragon'],
            'dragon': ['air', 'sponge', 'paper', 'tree', 'wolf', 'human', 'water'],
            'water': ['snake', 'sponge', 'paper', 'tree', 'wolf', 'human', 'air'],
            'air': ['snake', 'sponge', 'scissors', 'tree', 'wolf', 'human', 'paper'],
            'sponge': ['snake', 'scissors', 'tree', 'human', 'rock', 'fire', 'wolf'],
            'wolf': ['snake', 'scissors', 'human', 'rock', 'fire', 'gun', 'tree'],
            'tree': ['snake', 'scissors', 'rock', 'fire', 'gun', 'lightning', 'human'],
            'human': ['scissors', 'rock', 'fire', 'gun', 'lightning', 'devil', 'snake'],
            'snake': ['rock', 'fire', 'gun', 'lightning', 'devil', 'dragon', 'scissors'],
            'fire': ['fire', 'gun', 'lightning', 'devil', 'dragon', 'water', 'rock'],
        }
        self.all_simbols = ['fire', 'scissors', 'human', 'tree', 'wolf',
                            'sponge', 'paper', 'air', 'water', 'dragon',
                            'devil', 'lightning', 'gun', 'rock', 'snake']



    def rand_simbol(self, user, r):
        victory = True
        for word in self.simbols[user]:
            if word == r:
                victory = False
        return victory

    def who_win(self):
        user = str(input(">"))
        if user in self.pc:
            r = random.choice(self.pc)
            if user == r:
                print(f"There is a draw ({r})")
                self.resalt += 50
                self.who_win()
            elif self.rand_simbol(user, r):
                self.resalt += 100
                print(f"Well done. The computer chose {r} and failed")
                self.who_win()
            elif not self.rand_simbol(user, r):
                print(f"Sorry, but the computer chose {r}")
                self.who_win()
        elif user == "!rating":
            print(f"Your rating:{self.resalt}")
            self.who_win()
        elif user == "!exit":
            self.new_adds()
            print("Bay!")
            exit()
        else:
            print("Invalid input.")
            self.who_win()


    def init(self):
        print(f"Hello {self.name}")
        user_choise = str(input(">")).split(',')
        self.pc = user_choise
        if self.pc == ['']:
            self.pc = ['rock', 'paper', 'scissors']
        print("Okay, let's start")
        print(self.pc)
        with open("reting.txt", "r") as f:
            resalt = f.readlines()
            f.close()
            for i in range(0, len(resalt)):
                line = resalt[i].split()
                key = line[0]
                value = line[1]
                if key == self.name:
                    self.resalt = int(value)
        with open("reting.txt", "w") as f:
            for line in resalt:
                if line != f'{self.name} {self.resalt}\n':
                    f.write(line)
            f.close()


    def new_adds(self):
        with open("reting.txt", "a") as f:
            f.write(f'{self.name} {self.resalt}\n')
            f.close()


    def menu(self):
        self.init()
        self.who_win()


rock_paper_scissors = Rock_paper_scissors()
rock_paper_scissors.menu()
