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
elif lucky == 'No':
    print('No one is going to be lucky')


