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


    def player_move(self):
        player = input(">")
        try:
            int(player)
        except ValueError:
            print("Invalid input. Please try again.")
            self.player_move()
        else:
            if int(player) in range(-len(self.player), len(self.player) + 1):
                move = int(player)
                if move == 0:
                    if len(self.stok_domino) != 0:
                        self.player.append(self.stok_domino[0])
                        self.stok_domino.remove(self.stok_domino[0])
                        self.status = "computer"
                        self.chang_status()
                    else:
                        self.status = "computer"
                        self.chang_status()
                elif move > 0:
                    if self.player[move - 1][0] == self.snake[-1][1]:
                        self.snake.append(self.player[move - 1])
                        self.player.remove(self.player[move - 1])
                        self.status = "computer"
                        self.chang_status()
                    elif self.player[move - 1][1] == self.snake[-1][1]:
                        self.snake.append(self.player[move - 1][::-1])
                        self.player.remove(self.player[move - 1])
                        self.status = "computer"
                        self.chang_status()
                    else:
                        print("Illegal move. Please try again.")
                        self.chang_status()
                elif move < 0:
                    if self.player[-move - 1][1] == self.snake[0][0]:
                        self.snake.insert(0, self.player[-move - 1])
                        self.player.remove(self.player[-move - 1])
                        self.status = "computer"
                        self.chang_status()
                    elif self.player[-move - 1][0] == self.snake[0][0]:
                        self.snake.insert(0, self.player[-move - 1][::-1])
                        self.player.remove(self.player[-move - 1])
                        self.status = "computer"
                        self.chang_status()
                    else:
                        print("Illegal move. Please try again.")
                        self.player_move()
            else:
                print("Invalid input. Please try again.")
                self.player_move()


    def find_level(self, move):
        level = list(filter(lambda x: x[0] in move or x[1] in move, self.snake))
        level_pc = list(filter(lambda x: x[0] in move or x[1] in move, self.computer))
        level = len(level)+len(level_pc)
        return level


    def find_the_best(self, correct_moves):
        move = None
        level = 0
        for item in correct_moves:
            current_level = self.find_level(item)
            if level > current_level:
                continue
            move = item
            level = current_level

        return move


    def faind(self, move_pc):
        if self.snake[0][0] in move_pc:
            return True
        if self.snake[-1][1] in move_pc:
            return True


    def computer_move(self):
        computer = input(">")
        if computer == "":
            s = list(filter(self.faind, self.computer))
            if len(s) > 0:
                if self.find_the_best(s)[1] == self.snake[0][0]:
                    self.snake.insert(0, self.find_the_best(s))
                    self.computer.remove(self.find_the_best(s))
                    self.status = "player"
                    self.chang_status()
                elif self.find_the_best(s)[0] == self.snake[0][0]:
                    self.snake.insert(0, self.find_the_best(s)[::-1])
                    self.computer.remove(self.find_the_best(s))
                    self.status = "player"
                    self.chang_status()
                elif self.find_the_best(s)[0] == self.snake[-1][1]:
                    self.snake.insert(0, self.find_the_best(s))
                    self.computer.remove(self.find_the_best(s))
                    self.status = "player"
                    self.chang_status()
                elif self.find_the_best(s)[1] == self.snake[-1][1]:
                    self.snake.insert(0, self.find_the_best(s)[::-1])
                    self.computer.remove(self.find_the_best(s))
                    self.status = "player"
                    self.chang_status()
            elif len(s) < 1:
                self.computer.append(self.stok_domino[0])
                self.stok_domino.remove(self.stok_domino[0])
                self.status = "player"
                self.chang_status()
        else:
            print("Invalid input. Please try again.")


    def menu(self):
        self.random_domino()
        self.first_step()
        self.chang_status()



domino = Dominoes()
domino.menu()