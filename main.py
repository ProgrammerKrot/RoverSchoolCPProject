import ti_rover as rv 
import ti_plotlib as plt 
from math import *
from ti_system import *
from time import *
from random import *


choice = ""
while choice != "stop":
    rv.stop()
    print("choose from the following: ")
    choice = input()
    if choice == "1":
        print("entering maze... insert the command")
        n = input()
        while n != "back":
            notes = list(n)
            for elem in notes:
                if elem == "f":
                    print("moving forward")
                    rv.forward(3)
                elif elem == "r":
                    print("moving right")
                    rv.right(95)
                    rv.forward(3)
                elif elem == "l":
                    print("moving left")
                    rv.left(95)
                    rv.forward(3)
                elif elem == "b":
                    print("moving backwards")
                    rv.backwards(3)
            n = input()
    if choice == "2":
        print("opening drawing...")
        print("available shapes: square, triangle, circle. Put the first letter")
        n = input()
        while n != "back":
            if n == "s":
                print("enter its width and height")
                w = int(input())
                h = int(input())
                for i in range(0, 2):
                    rv.forward(h)
                    rv.right(90)
                    rv.forward(w)
                    rv.right(90)
                n = input()
            if n == "t":
                print("enter length of trinagle")
                l = int(input())
                for i in range(0, 3):
                    rv.left(120)
                    rv.forward(l)
                n =input()
            if n == "c":
                print("sorry, but he left us:(")
                n = "back"
    if choice = "3":
        print("entering avoider..")
        print("ready to start")
        while get_key() != "7":
            decision = randint(1, 2)
            ob = rv.rangermeasurement()
            if ibs <= 0.1:
                if decision == 1:
                    rv.stop()
                    rv.backwards(2)
                    rv.right(90)
                    rv.forward(100)
                    sleep(5)
                else:
                    rv.stop()
                    rv.backwards(2)
                    rv.left(90)
                    rv.forward(100)
                    sleep(5)
    if choice == "4":
        print("entering drift mode")
        while True:
            rv.left(360)
            sleep(2)
            rv.stop()