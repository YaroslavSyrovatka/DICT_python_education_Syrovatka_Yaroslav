import random


class Arithmetic_test:


    def __init__(self):
        self.user = None
        self.mark = 0
        self.trys = 0
        self.lvl = None


    def mult(self, b, c):
        print(f"{b} * {c}")
        f = b * c
        self.check_1(f)


    def add(self, b, c):
        print(f"{b} + {c}")
        f = b + c
        self.check_1(f)


    def minus(self, b, c):
        print(f"{b} - {c}")
        f = b - c
        self.check_1(f)


    def chose_lvl(self):
        level = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
>""")
        self.lvl = level
        if self.lvl == "1":
            self.lvl = "1 (simple operations with numbers 2-9)."
            self.calc()
        elif self.lvl == "2":
            self.lvl = "2 (integral squares of 11-29)."
            self.sqrt()
        else:
            print("Incorrect format.")
            self.chose_lvl()


    def sqrt(self):
        n = random.randint(11, 29)
        print(n)
        f = n**2
        self.check_2(f)



    def calc(self):
        z = random.randint(2, 9)
        x = random.randint(2, 9)
        q = random.randint(1, 3)
        if q == 1:
            self.mult(z, x)
        elif q == 2:
            self.add(z, x)
        else:
            self.minus(z, x)



    def check_1(self, pc):
        self.correct_user()
        while self.trys != 5:
            if self.user == pc:
                self.mark += 1
                self.trys += 1
                print("Right!")
                self.correct_calc()
            else:
                self.trys += 1
                print("Wrong!")
                self.correct_calc()


    def check_2(self, pc):
        self.correct_user()
        while self.trys != 5:
            if self.user == pc:
                self.mark += 1
                self.trys += 1
                print("Right!")
                self.correct_sqrt()
            else:
                self.trys += 1
                print("Wrong!")
                self.correct_sqrt()

    def correct_calc(self):
        if self.trys == 5:
            return
        else:
            self.calc()


    def correct_sqrt(self):
        if self.trys == 5:
            return
        else:
            self.sqrt()


    def test(self):
        print(f"Your mark is {self.mark}/{self.trys}.Would you like to save the result? Enter yes or no.")
        write = input(">")
        alowed = ["y", "yes", "YES", "Yes"]
        for i in alowed:
            if write == i:
                name = input(">")
                file = open("results.txt", "a")
                file.write(f"{name}: {self.mark}/{self.trys} in level{self.lvl}\n")
                file.close()
                print("The results are saved in ""results.txt"".")
            else:
                exit()





    def correct_user(self):
        try:
            self.user = int(input(">"))
        except ValueError:
            print("Incorrect format.")
            self.correct_user()

    def menu(self):
        self.chose_lvl()
        self.test()


a = Arithmetic_test()
a.menu()
