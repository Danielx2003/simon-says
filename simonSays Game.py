import random
from random import randint
from random import choices
import time

def delay(delayTime):
    time.sleep(delayTime)

    for i in range(15):
        print("\n")

    return None

def userInput(sequence, num):
    print("enter the sequence you just saw on seperate lines")
    userIn = []
    for i in range(num):
        user = str(input("enter the letter of the colour")).lower()

        if user == "r":
            userIn.append("red")

        if user == "g":
            userIn.append("green")

        if user == "p":
            userIn.append("purple")

        if user == "b":
            userIn.append("blue")


    if userIn == sequence:
        print("Correct")
        print("\n")
        time.sleep(2)
    else:
        print("You scored, ",num-1)
        quit()


def sequenceGenerator(num, delayTime):
    TWHITE = '\033[37m'
    TGREEN = '\033[32m'
    TPURPLE = '\033[35m'
    TRED = '\033[31m'
    TBLUE = '\033[34m'
    time.sleep(0.75)
    sequence = []
    for i in range(num):
        time.sleep(0.5)
        string = ",".join(random.choices(colours))
        if string == "green":
            print(TGREEN + string, TWHITE)
            sequence.append(string)

        if string == "red":
            print(TRED + string, TWHITE)
            sequence.append(string)

        if string == "blue":
            print(TBLUE + string, TWHITE)
            sequence.append(string)

        if string == "purple":
            print(TPURPLE + string, TWHITE)
            sequence.append(string)

    delay(delayTime)


    userInput(sequence,num)

    return None

endGame = False
num = 0
delayTime = 1.5
while endGame == False:
    colours = ["red", "blue", "green", "purple"]
    string = ""
    num += 1
    if delayTime > 0.5:
        delayTime -= 0.
    sequenceGenerator(num, delayTime)





