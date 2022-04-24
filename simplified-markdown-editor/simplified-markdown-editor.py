class Markdown:
    def __init__(self):
        self.formats = ("plain", "bold", "italic", "header",
                        "link", "inline-code", "ordered-list",
                        "unordered-list", "new-line")
        self.comand = ("!help", "!done")


    def init(self):
        user_comand = input("Choose a formatter:>")
        if user_comand == self.comand[0]:
            print("Available formatters:", *self.formats)
            print("Special commands:", *self.comand)
            self.init()
        elif user_comand == self.comand[1]:
            self.init()
        elif user_comand in self.formats:
            self.init()
        else:
            print("Unknown formatting type or command")
            self.init()


    def menu(self):
        self.init()



m = Markdown()
m.menu()

