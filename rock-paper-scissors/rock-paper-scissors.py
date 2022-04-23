import random


class Rock_paper_scissors:
    simbols = {
        'rock': ['paper'],
        'paper': ['scissors'],
        'scissors': ['rock'],
    }

    def __init__(self):
        self.pc = ['rock', 'paper', 'scissors']




    def who_win(self):
        user = str(input(">"))
        r = random.choice(self.pc)
        if user == r:
            print(f"There is a draw ({r})")
            return
        for i in self.simbols[user]:
            if i == r:
                print(f"Sorry, but the computer chose {r}")
            elif i != r:
                print(f"Well done. The computer chose {r} and failed")


    def menu(self):
        self.who_win()


rock_paper_scissors = Rock_paper_scissors()
rock_paper_scissors.menu()
