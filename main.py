# Last edited by Robert Hollinger 10/17/2020
import tkinter as tk
from time import *

# If player = True, then it is 'X' turn; if False then it's 'O' turn
player = True
# counts how many turns, if == 9, then game over
count = 0


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
        self.master = master
        self.pack()
        self.create_widgets()

    def click(self, b):
        global player, count
        if b["text"] == " " and player is True:
            b["text"]= "X"
            player = False
            count += 1
        elif b["text"] == " " and player is False:
            b["text"] = "O"
            player = True
            count += 1
        self.check_for_win()

    def check_for_win(self):
        # check for horizontal win for X
        if self.b1["text"] == "X" and self.b2["text"] == "X" and self.b3["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b4["text"] == "X" and self.b5["text"] == "X" and self.b6["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b7["text"] == "X" and self.b8["text"] == "X" and self.b9["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        # Check for horizontal O win
        elif self.b1["text"] == "O" and self.b2["text"] == "O" and self.b3["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b4["text"] == "O" and self.b5["text"] == "O" and self.b6["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b7["text"] == "O" and self.b8["text"] == "O" and self.b9["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()

        # check for vertical win for X
        elif self.b1["text"] == "X" and self.b4["text"] == "X" and self.b7["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b2["text"] == "X" and self.b5["text"] == "X" and self.b8["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b3["text"] == "X" and self.b6["text"] == "X" and self.b9["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        # check for vertical win for O
        elif self.b1["text"] == "O" and self.b4["text"] == "O" and self.b7["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b2["text"] == "O" and self.b5["text"] == "O" and self.b8["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b3["text"] == "O" and self.b6["text"] == "O" and self.b9["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()

        # check for diagonal win for X
        elif self.b1["text"] == "X" and self.b5["text"] == "X" and self.b9["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b3["text"] == "X" and self.b5["text"] == "X" and self.b7["text"] == "X":
            print("Congratulations, player X won!")
            win = tk.Label(self, text="Congratulations, player X won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()

        elif self.b1["text"] == "O" and self.b5["text"] == "O" and self.b9["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()
        elif self.b3["text"] == "O" and self.b5["text"] == "O" and self.b7["text"] == "O":
            print("Congratulations, player O won!")
            win = tk.Label(self, text="Congratulations, player O won!")
            win.grid(row=5, column=1, rowspan=3)
            exit()

    def create_widgets(self):
        # Once button is pressed it calls method click() and passes the current button to it
        # Click() updates the button with X or O
        self.b1 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b1))
        self.b2 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b2))
        self.b3 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b3))
        self.b4 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b4))
        self.b5 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b5))
        self.b6 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b6))
        self.b7 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b7))
        self.b8 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b8))
        self.b9 = tk.Button(self, text=" ", height=3, width=6, command=lambda: self.click(self.b9))

        self.b1.grid(row=1, column=0)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)
        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)
        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)


def main():
    root = tk.Tk()
    application = Application(root)

    application.mainloop()


if __name__ == '__main__':
    main()


