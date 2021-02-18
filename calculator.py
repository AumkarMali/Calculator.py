
import re

print("python calculator")
print("type 'quit' to exit")

previous = 0
run = True

def math():
    global run
    global previous
    equat =""
    if previous == 0:
       equat = input("enter equation")
    else:
        equat = input(str(previous))
    if equat == 'quit':
        print("Program Shut down")
        run = False
    else:
        equat = re.sub('[A-Za-z,.:;()" "]', '', equat)
    if previous == 0:
        previous = eval(equat)
    else:
        previous = eval(str(previous) + equat)

while run:
    math()