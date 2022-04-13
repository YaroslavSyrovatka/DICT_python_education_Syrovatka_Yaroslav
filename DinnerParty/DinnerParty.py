import random

number = int(input('Enter the number of friends joining (including you):\n>'))
frends = {}
if number > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(number):
        name = input('>')
        frends[name] = 0
else:
    print('No one is joining for the party')
    exit()
amount = int(input('Enter the total amount:\n>'))
lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n>')
if lucky == 'Yes':
    random_friend = random.choice(list(frends.keys()))
    print(f"{random_friend} is the lucky one!")
    cost = round(amount / (number-1), 2)
    if int(cost) != cost:
        a = round(amount / (number-1), 2)
    else:
        a = round(amount / (number-1))
    for name in frends:
        frends[name] = a
    frends[random_friend] = 0
    print(frends)
elif lucky == 'No':
    print('No one is going to be lucky')
    cost = round(amount / number, 2)
    if int(cost) != cost:
        a = round(amount/number, 2)
    else:
        a = round(amount/number)
    for name in frends:
        frends[name] = a
    print(frends)


