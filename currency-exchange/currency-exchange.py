class Exchange:
    def __init__(self):
        self.mycoins = 0
        self.rate = 0
        self.amount = 0


    def init(self):
        coins_input = int(input("Please, enter the number of mycoins you have:>"))
        self.mycoins = coins_input
        rate_input = float(input("Please, enter the exchange rate:>"))
        self.rate = rate_input
        self.amount = self.mycoins * self.rate
        print(f"The total amount of dollars:{self.amount}")


    def menu(self):
        self.init()


e = Exchange()
e.menu()