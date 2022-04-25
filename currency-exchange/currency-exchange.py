import requests
import json



class Exchange:
    def __init__(self):
        ...


    def init(self):
        coins = float(input("Now mach you have>"))
        curreny = input("name currency>")
        response = requests.get(f"http://www.floatrates.com/daily/{curreny}.json")
        other_corr = response.json()
        d = other_corr.get("usd").get("rate")
        e = other_corr.get("eur").get("rate")
        print("eur", round(coins * e, 2))
        print("usd", round(coins * d, 2))




    def menu(self):
        self.init()


e = Exchange()
e.menu()