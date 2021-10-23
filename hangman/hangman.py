import random
print("HANGMAN")
# print("The game will be available soon.")


def stag_1():
    words = ["space", "human", "woman", "bulldozer"]
    a = input("Guess the word:>")
    if a == words[1]:
        print("You survived!")
    else:
        print("You lost!")


# stag_1()


def stag_2():
    words = ["space", "human", "woman", "bulldozer"]
    a = input("Guess the word:>")
    if a == random.choice(words):
        print("You survived!")
    else:
        print("You lost!")


# stag_2()

def stag_3():
    words = ["space", "human", "woman", "bulldozer"]
    s = random.choice(words)
    w = "-" * len(s[3:])
    # print(s[:3]+w)
    a = input("Guess the word "+(s[:3]+w)+":>")
    if a == s:
        print("You survived!")
    else:
        print("You lost!")


# stag_3()