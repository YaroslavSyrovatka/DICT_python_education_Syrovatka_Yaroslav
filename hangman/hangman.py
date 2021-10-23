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