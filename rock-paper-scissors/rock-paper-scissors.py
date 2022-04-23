class Rock_paper_scissors:
    def __init__(self):
        self.player = None


    def pc_win(self):
        user = str(input(">"))
        if user == "rock":
            print(f"Sorry, but the computer chose paper")
        elif user == "paper":
            print(f"Sorry, but the computer chose scissors")
        elif user == "scissors":
            print(f"Sorry, but the computer chose rock")


    def menu(self):
        self.pc_win()


rock_paper_scissors = Rock_paper_scissors()
rock_paper_scissors.menu()
