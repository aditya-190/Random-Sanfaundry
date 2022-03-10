import json
import random
import re
import tkinter
import webbrowser


# 1. DSA
# 2. Python
# 3. Java
# 4. C++
# 5. C
# 6. OOPS
# 7. LINUX
# 8. MONGODB
# 9. MYSQL
# 10 .COMPUTER FUNDAMENTAL\n11. OS
# 12. COMPUTER NETWORK
# 13. DBMS
# 14. RDBMS
# 15. HTML
# 16. CSS
# 17. JAVASCRIPT"

class EntryWithPlaceholder(tkinter.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self):
        if not self.get():
            self.put_placeholder()


def screen():
    top = tkinter.Tk()
    top.title("Random Sanfaundry Pages")
    top.geometry("500x150")

    label = tkinter.Label(top, text="Enter Details", font="Courier 22 bold")
    label.pack()

    section = EntryWithPlaceholder(top, "Enter Section")
    section.pack()

    topic = EntryWithPlaceholder(top, "Enter Topic")
    topic.pack()

    tkinter.Button(top, text="Get Page", width=20, command=lambda: select_random_url(section, topic),
                   highlightbackground='#3E4149').pack(pady=20)

    top.mainloop()


def escape_special_characters(inputString):
    return inputString.translate(str.maketrans(
        {"+": r"\+", "-": r"\-", "]": r"\]", "\\": r"\\", "^": r"\^", "$": r"\$", "*": r"\*", ".": r"\."}))


def select_random_url(section, topic):
    section = section.get().strip()
    topic = topic.get().strip()

    if section == "Enter Section":
        section = ""

    if topic == "Enter Topic":
        topic = ""

    section = escape_special_characters(section)
    topic = escape_special_characters(topic)

    data = json.load(open('list.json'))
    temporary = data

    if section:
        temporary = list(filter(lambda datum: re.search(section, datum["Section"], re.IGNORECASE), temporary))

    if topic:
        temporary = list(filter(lambda datum: re.search(topic, datum["Topic"][0], re.IGNORECASE), temporary))

    if temporary:
        webbrowser.open(url=random.choice(temporary)["URL"][0])

    else:
        webbrowser.open(url=random.choice(data)["URL"][0])


screen()
