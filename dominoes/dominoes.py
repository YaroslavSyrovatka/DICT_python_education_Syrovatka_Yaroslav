import random


class Dominoes:
    def __init__(self):
        self.all_bone = [[z, x] for z in range(7) for x in range(z, 7)]
        self.stok_domino = []
        self.player = []
        self.computer = []
        self.snake = []
        self.status = None

    def print_plaer(self):
        for i in range(len(self.player)):
            print(f"{i + 1}:", self.player[i])


    def interface(self):
        """тут будет то вывод данных"""
        print(f"-"*70)
        print(f"Stock size: {self.stok_domino}")
        print(f"Computer pieces: {self.computer}")
        if len(self.snake) > 6:
            print(*self.snake[:3], "...", *self.snake[-3:], sep="")
        else:
            print(*self.snake, sep="")
        print("Your pieces:")
        self.print_plaer()
        if self.status == "player":
            print("Status: It's your turn to make a move. Enter your command.")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")


    def random_domino(self):
        """тут домно разделяются рандомно"""
        a = random.sample(self.all_bone, 28)
        self.player = a[0:7]
        self.computer = a[7:14]
        self.stok_domino = a[14:28]


    def chang_status(self):
        if self.status == "computer":
            self.who_wins()
            self.interface()
            self.computer_move()
        elif self.status == "player":
            self.who_wins()
            self.interface()
            self.player_move()


    def first_step(self):
        """эта функция выдет первый дубль"""
        a = list(filter(lambda x: x[0] == x[1], self.player))
        b = list(filter(lambda x: x[0] == x[1], self.computer))
        if len(a) == 0 and len(b) == 0:
            self.menu()
            return
        elif len(a) > 0 and len(b) > 0 and max(a) > max(b):
            self.snake.append(max(a))
            self.player.remove(max(a))
            self.status = "computer"
        elif len(a) > 0 and len(b) > 0 and max(b) > max(a):
            self.snake.append(max(b))
            self.computer.remove(max(b))
            self.status = "player"
        elif len(a) > 0 and len(b) == 0:
            self.snake.append(max(a))
            self.player.remove(max(a))
            self.status = "computer"
        elif len(b) > 0 and len(a) == 0:
            self.snake.append(max(b))
            self.computer.remove(max(b))
            self.status = "player"


    def who_wins(self):
        if len(self.player) == 0:
            self.status = "The game is over. You won!"
            print(f"Status: {self.status}")
            exit()
        elif len(self.computer) == 0:
            self.status = "The game is over. The computer won!"
            print(f"Status: {self.status}")
            exit()
        elif self.snake[0][0] == self.snake[-1][-1]:
            count = 0
            for item in range(len(self.snake)):
                for i in self.snake[item]:
                    if i == self.snake[0][0]:
                        count += 1
            if count == 8:
                self.status = "The game is over. It's a draw!"
                print(f"Status: {self.status}")
                exit()


    def menu(self):
        self.random_domino()
        self.first_step()
        self.chang_status()



domino = Dominoes()
domino.menu()