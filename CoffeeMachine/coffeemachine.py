# def stage_1():
#     print('''Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!''')
#
#
# stage_1()
# def stage_2():
#     cap = int(input("Write how many cups of coffee you will need:>"))
#     water = 200
#     mailk = 50
#     coffee = 15
#     s = cap * water
#     a = cap * mailk
#     d = cap * coffee
#     print("For", cap, "cups of coffee you will need:\n", s, "ml of water\n", a, "ml of milk\n", d,
#     "g of  coffee beans")
#
#
# stage_2()
# def stage_3():
#     water = int(input("Write how many ml of water the coffee machine has:\n>"))
#     milk = int(input("Write how many ml of milk the coffee machine has:\n>"))
#     coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n>"))
#     cups = int(input("Write how many cups of coffee you will need:\n>"))
#     if water//200 == cups and milk//50 == cups and coffee//15 == cups:
#         print("Yes, I can make that amount of coffee")
#     elif water//200 > cups and milk//50 > cups and coffee//15 > cups:
#         F = min(water//200, milk//50, coffee//15)
#         N = F - cups
#         print("Yes, I can make that amount of coffee (and even", N, "more than that)")
#     else:
#         F = min(water//200, milk//50, coffee//15)
#         print("No, I can make only", F, "cups of coffee")
#
#
# stage_3()
# water = 400
# milk = 540
# coffee = 120
# cups = 9
# money = 550
#
#
# def ingredents():
#     print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n", cups,
#           "of disposable cups\n", money, "of money")
#     return input("Write action (buy, fill, take):\n>")
#
#
# def buys():
#     global water, milk, coffee, cups, money
#     z = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n>"))
#     if z == 1:
#         water = water - 250
#         coffee = coffee - 16
#         cups = cups - 1
#         money = money + 4
#         print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n",
#               cups, "of disposable cups\n", money, "of money")
#     if z == 2:
#         water = water - 350
#         milk = milk - 75
#         coffee = coffee - 20
#         cups = cups - 1
#         money = money + 7
#         print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n",
#               cups, "of disposable cups\n", money, "of money")
#     if z == 3:
#         water = water - 200
#         milk = milk - 100
#         coffee = coffee - 12
#         cups = cups - 1
#         money = money + 6
#         print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n",
#               cups, "of disposable cups\n", money, "of money")
#
#
# def fills():
#     global water, milk, coffee, cups, money
#     c = int(input("Write how many ml of water you want to add:\n>"))
#     water = water + c
#     v = int(input("Write how many ml of milk you want to add:\n>"))
#     milk = milk + v
#     b = int(input("Write how many grams of coffee beans you want to add:\n>"))
#     coffee = coffee + b
#     n = int(input("Write how many disposable coffee cups you want to add:\n>"))
#     cups = cups + n
#     print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n", cups,
#           "of disposable cups\n", money, "of money")
#
#
# def takes():
#     global water, milk, coffee, cups, money
#     print("I gave you", money,)
#     money = money - money
#     print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n", cups,
#           "of disposable cups\n", money, "of money")
#
#
# def main():
#     ing = ingredents()
#     if ing == "buy":
#         buys()
#     elif ing == "fill":
#         fills()
#     elif ing == "take":
#         takes()
#
#
# main()
water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def ingredents():
    return input("Write action (buy, fill, take,remaining,exit):\n>")


def remaining():
    print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee, "of coffee beans\n", cups,
          "of disposable cups\n", money, "of money")


def buys():
    global water, milk, coffee, cups, money
    z = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n>"))
    if z == "1":
        water = water - 250
        coffee = coffee - 16
        cups = cups - 1
        money = money + 4
        if water < 0:
            print("Sorry, not enough water!")
        elif coffee < 0:
            print("Sorry, not enough coffee!")
        elif cups < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
    elif z == "2":
        water = water - 350
        milk = milk - 75
        coffee = coffee - 20
        cups = cups - 1
        money = money + 7
        if water < 0:
            print("Sorry, not enough water!")
        elif coffee < 0:
            print("Sorry, not enough coffee!")
        elif cups < 0:
            print("Sorry, not enough cups!")
        elif milk < 0:
            print("Sorry, not enough milk!")
        else:
            print("I have enough resources, making you a coffee!")
    elif z == "3":
        water = water - 200
        milk = milk - 100
        coffee = coffee - 12
        cups = cups - 1
        money = money + 6
        if water < 0:
            print("Sorry, not enough water!")
        elif coffee < 0:
            print("Sorry, not enough coffee!")
        elif cups < 0:
            print("Sorry, not enough cups!")
        elif milk < 0:
            print("Sorry, not enough milk!")
        else:
            print("I have enough resources, making you a coffee!")
    elif z == "back":
        ingredents()


def fills():
    global water, milk, coffee, cups, money
    c = int(input("Write how many ml of water you want to add:\n>"))
    water = water + c
    v = int(input("Write how many ml of milk you want to add:\n>"))
    milk = milk + v
    b = int(input("Write how many grams of coffee beans you want to add:\n>"))
    coffee = coffee + b
    n = int(input("Write how many disposable coffee cups you want to add:\n>"))
    cups = cups + n


def takes():
    global water, milk, coffee, cups, money
    print("I gave you", money,)
    money = money - money


def main():
    ing = ingredents()
    if ing == "buy":
        buys()
        main()
    elif ing == "fill":
        fills()
        main()
    elif ing == "take":
        takes()
        main()
    elif ing == "remaining":
        remaining()
        main()
    elif ing == "exit":
        exit()


main()