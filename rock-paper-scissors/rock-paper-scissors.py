import random


class Rock_paper_scissors:
    simbols = {
        'rock': ['paper'],
        'paper': ['scissors'],
        'scissors': ['rock'],
    }

    def __init__(self):
        self.pc = ['rock', 'paper', 'scissors']


    def check_simbols(self, user, pc):
        for i in self.simbols[user]:
            if i == pc:
                print(f"Sorry, but the computer chose {pc}")
                self.who_win()
            elif i != pc:
                print(f"Well done. The computer chose {pc} and failed")
                self.who_win()


    def who_win(self):
        user = str(input(">"))
        if user in self.pc:
            r = random.choice(self.pc)
            if user == r:
                print(f"There is a draw ({r})")
                self.who_win()
                return
            elif user == "!exit":
                print("Bay!")
                exit()
            else:
                self.check_simbols(user, r)
        else:
            print("Invalid input.")
            self.who_win()



    def menu(self):
        self.who_win()


rock_paper_scissors = Rock_paper_scissors()
rock_paper_scissors.menu()
