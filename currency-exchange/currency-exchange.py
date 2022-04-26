import requests


class Exchange:
    def __init__(self):
        self.cash = dict()
        self.exchange_currency = None


    def init(self):
        wanted_currrency = input(">").lower()
        coins = self.correct_float_input()
        print("Checking the cache...")
        response = requests.get(f"http://www.floatrates.com/daily/{self.exchange_currency}.json")
        if response.ok:
            result = response.json()
            self.cash['eur'] = result.get("rate")
            self.cash['usd'] = result.get("rate")
            try:
                result = result.get(f"{wanted_currrency}").get("rate")
            except AttributeError:
                print("Incorrect second parameter")
                self.init()
            if wanted_currrency in self.cash:
                print("It is in the cache!")
                print(f"You received {round(coins * result, 2)} {wanted_currrency.upper()}.")
                self.init()
            else:
                print("Sorry, but it is not in the cache!")
                print(f"You received {round(coins * result, 2)} {wanted_currrency.upper()}.")
                self.cash[wanted_currrency] = result
                self.init()
        else:
            print("Incorrect fitst parameter")
            self.menu()


    def correct_float_input(self):
        user_input = input(">")
        while True:
            try:
                float(user_input)
            except ValueError:
                if "," in user_input:
                    user_input = user_input.replace(",", ".")
                    continue
                print("Incorrect format")
                user_input = input(">")
                continue
            else:
                break
        return float(user_input)


    def menu(self):
        self.exchange_currency = input(">").lower()
        self.init()


e = Exchange()
e.menu()