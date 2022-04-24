class Markdown:
    def __init__(self):
        self.formats = ("plain", "bold", "italic", "header",
                        "link", "inline-code", "ordered-list",
                        "unordered-list", "new-line")
        self.comand = ("!help", "!done")
        self.resalt = ""


    def cheng_txt(self):
        file = open("output.md", "w")
        file.write(self.resalt)
        file.close()


    def init(self):
        user_comand = input("Choose a formatter:>")
        if user_comand == self.comand[0]:
            print("Available formatters:", *self.formats)
            print("Special commands:", *self.comand)
            self.init()
        elif user_comand == self.comand[1]:
            self.cheng_txt()
        elif user_comand == self.formats[0]:
            user_input = input("Text:>")
            self.resalt += f"{user_input}"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[1]:
            user_input = input("Text:>")
            self.resalt += f"**{user_input}**"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[2]:
            user_input = input("Text:>")
            self.resalt += f"*{user_input}*"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[3]:
            lvl = self.lvl_correct()
            user_input = input("Text:>")
            self.resalt += f"{lvl * '#'} {user_input}\n"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[4]:
            label = input("Label:>")
            url = input("url")
            self.resalt += f"[{label}]({url})"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[5]:
            user_input = input("Text:>")
            self.resalt += f"```{user_input}``` "
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[6]:
            rows = self.rows_correct()
            for row in range(1, rows + 1):
                user_input = input(f"Row #{row}: > ")
                self.resalt += f"{row}. {user_input}  \n"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[7]:
            rows = self.rows_correct()
            for row in range(1, rows + 1):
                user_input = input(f"Row #{row}: > ")
                self.resalt += f"* {user_input}  \n"
            print(self.resalt)
            self.init()
        elif user_comand == self.formats[8]:
            self.resalt += "\n"
            print(self.resalt)
            self.init()
        else:
            print("Unknown formatting type or command")
            self.init()


    def lvl_correct(self):
        lvl = input("Level:>")
        while lvl:
            try:
                lvl = int(lvl)
            except ValueError:
                print("Please input number")
                lvl = input("Level:>")
                continue

            else:
                lvl = int(lvl)
                if not 0 < lvl <= 6:
                    print("The level should be within the range of 1 to 6.")
                    lvl = input("Level:>")
                    continue
                break

        return lvl


    def rows_correct(self):
        rows = input("Number of rows: > ")
        while rows:
            try:
                rows = int(rows)
            except ValueError:
                print("Please input number")
                rows = input("Number of rows: > ")
                continue

            else:
                rows = int(rows)
                if not 0 < rows:
                    print("Number rows cannot be negative")
                    rows = input("Number of rows: > ")
                    continue
                break

        return rows

    def menu(self):
        self.init()



m = Markdown()
m.menu()

