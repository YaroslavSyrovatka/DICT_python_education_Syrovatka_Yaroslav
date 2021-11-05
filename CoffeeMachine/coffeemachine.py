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
def stage_2():
    cap = int(input("Write how many cups of coffee you will need:>"))
    water = 200
    mailk = 50
    coffee = 15
    s = cap * water
    a = cap * mailk
    d = cap * coffee
    print("For", cap, "cups of coffee you will need:\n", s, "ml of water\n", a, "ml of milk\n", d, "g of  coffee beans")


stage_2()
