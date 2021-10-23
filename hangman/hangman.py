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


def stag_4():
    words = ["space", "human", "woman", "bulldozer"]
    word = random.choice(words)
    under = "_" * len(word)
    guessed = False
    tries = 8
    guessed_letters = []
    print(under)
    while not guessed and tries > 0:
        guess = input("Input a letter: >").lower()
        if len(guess) == 1:
            if guess in word:
                guessed_letters.append(guess)
                word_as_list = list(under)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                under = "".join(word_as_list)
                if "_" not in under:
                    print("The word is", word, "\nYou win")
                    break
                tries -= 1
                print(under)
            else:
                tries -= 1
                print("That letter doesn't appear in the word")
    else:
        print("Thanks for playing!\nWe'll see how well you did in the next stage")


# stag_4()