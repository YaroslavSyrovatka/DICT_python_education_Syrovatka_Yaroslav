class Exchange:
    def __init__(self):
        ...


    def init(self):
        coins_input = float(input(">"))
        s = "%g" % coins_input
        ars = round(coins_input * 0.1, 2)
        hnl = round(coins_input * 45.2, 2)
        aud = round(coins_input * 1.37, 2)
        mad = round(coins_input * 0.9991, 2)
        print(f"I will get {ars} ARS from the sale of {s} mycoins.")
        print(f"I will get {hnl} HNL from the sale of {s} mycoins.")
        print(f"I will get {aud} AUD from the sale of {s} mycoins.")
        print(f"I will get {mad} MAD from the sale of {s} mycoins.")



    def menu(self):
        self.init()


e = Exchange()
e.menu()