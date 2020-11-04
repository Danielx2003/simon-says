from tkinter import *
import random

fontType = ("Verdana", 12)

class window:

    def __init__(self, master, length, time):
        self.master = master
        master.title("Simon")

        self.time = time
        self.length = length

        self.label = Label(text="Score:", font=fontType)
        self.label.place(x=128,y=330)
        self.score = Label(font=fontType)
        self.score.place(x=180,y=330)

        self.b1 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("1"))
        self.b1.place(x=10, y=10)
        self.b2 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("2"))
        self.b2.place(x=120, y=10)
        self.b3 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("3"))
        self.b3.place(x=230, y=10)
        self.b4 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("4"))
        self.b4.place(x=10, y=120)
        self.b5 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("5"))
        self.b5.place(x=120, y=120)
        self.b6 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("6"))
        self.b6.place(x=230, y=120)
        self.b7 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("7"))
        self.b7.place(x=10, y=230)
        self.b8 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("8"))
        self.b8.place(x=120, y=230)
        self.b9 = Button(master, width=12, height=6, bg="grey", relief=RIDGE, activebackground="blue",
                         command=lambda: self.userInput("9"))
        self.b9.place(x=230, y=230)

        self.sequence(length)
        self.b1.after(time, lambda: self.compare(length))

    def compare(self, length):
        with open("userInput.txt", "r") as f:
            User = f.read()

        with open("AI Sequence.txt", "r") as f:
            AI = f.read()

        game = True


        for i in range(length):
            try:
                if User[i] == AI[i]:
                    game = True
                else:
                    game = False
            except:
                game = False
                pass

        if game == True:
            self.score.configure(text=(self.length))
            root.after(100, x.__init__(root, (length+1), (time+3500)))

        else:
            print("Game over")
            root.destroy()



    def userInput(self, num):
        with open("userInput.txt", "a") as f:
            if num == "1":
                f.write(num)
            if num == "2":
                f.write(num)
            if num == "3":
                f.write(num)
            if num == "4":
                f.write(num)
            if num == "5":
                f.write(num)
            if num == "6":
                f.write(num)
            if num == "7":
                f.write(num)
            if num == "8":
                f.write(num)
            if num == "9":
                f.write(num)



    def sequence(self, length):
        with open("AI Sequence.txt", "w") as f:
            f.close()

        with open("userInput.txt", "w") as f:
            f.close()

        num = 1000

        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(length):
            string = "".join(random.choices(numbers))
            num += 1000

            with open("AI Sequence.txt","a") as f:
                f.write(string)

            if string == "1":
                self.b1.after(num, lambda: self.b1.configure(background="red"))
                self.b1.after((num+750), lambda: self.b1.configure(background="grey"))

            if string == "2":
                self.b2.after(num, lambda: self.b2.configure(background="red"))
                self.b2.after((num+750), lambda: self.b2.configure(background="grey"))

            if string == "3":
                self.b3.after(num, lambda: self.b3.configure(background="red"))
                self.b3.after((num+750), lambda: self.b3.configure(background="grey"))

            if string == "4":
                self.b4.after(num, lambda: self.b4.configure(background="red"))
                self.b4.after((num+750), lambda: self.b4.configure(background="grey"))

            if string == "5":
                self.b5.after(num, lambda: self.b5.configure(background="red"))
                self.b5.after((num+750), lambda: self.b5.configure(background="grey"))

            if string == "6":
                self.b6.after(num, lambda: self.b6.configure(background="red"))
                self.b6.after((num+750), lambda: self.b6.configure(background="grey"))

            if string == "7":
                self.b7.after(num, lambda: self.b7.configure(background="red"))
                self.b7.after((num+750), lambda: self.b7.configure(background="grey"))

            if string == "8":
                self.b8.after(num, lambda: self.b8.configure(background="red"))
                self.b8.after((num+750), lambda: self.b8.configure(background="grey"))

            if string == "9":
                self.b9.after(num, lambda: self.b9.configure(background="red"))
                self.b9.after((num+750), lambda: self.b9.configure(background="grey"))

length = 1
time = 7500
root = Tk()
root.geometry("335x400")
x = window(root, length, time)
root.mainloop()




