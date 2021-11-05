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
def stage_3():
    water = int(input("Write how many ml of water the coffee machine has:\n>"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n>"))
    coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n>"))
    cups = int(input("Write how many cups of coffee you will need:\n>"))
    if water//200 == cups and milk//50 == cups and coffee//15 == cups:
        print("Yes, I can make that amount of coffee")
    elif water//200 > cups and milk//50 > cups and coffee//15 > cups:
        F = min(water//200, milk//50, coffee//15)
        N = F - cups
        print("Yes, I can make that amount of coffee (and even", N, "more than that)")
    else:
        F = min(water//200, milk//50, coffee//15)
        print("No, I can make only", F, "cups of coffee")


stage_3()
