import ti_rover as rv #main lib for communication with rover
import ti_plotlib as plt #extra stuff like sensors
from math import *           #additional math functions - python have lots of libraries(libs) - additional pack of functions and commands, here i imported them all
from ti_system import * #one more library for rover, now for connecting
from time import * #library, that I used to give some rest to my program, using sleep()
from random import * #easy to guess, for all random, you can blame this lib. I used it for random side in avoider part

#sometime you see sleep() - I use it that a memory overflow doesnt occur, and rover has a time to rest between commands

choice = ""   
while choice != "stop":
    rv.stop() #I used rv.stop every time then I need to clean up memory of the rover and make it "forget" previous 
    print("choose from the following: ")
    choice = input()
    if choice == "1":
        print("entering maze... insert the command")
        n = input()
        while n != "back":
            notes = list(n) # commands should have be written like fswb. list will divide each, and Ill get a clear list of it
            for elem in notes: #to run each of it separately!
                if elem == "f":
                    print("moving forward")
                    rv.forward(3)
                elif elem == "r":
                    print("moving right")
                    rv.right(95) #its not the right angle, however I make additional 5 degrees, because rover tends to rotate unfinished depending on a surface
                    rv.forward(3)
                elif elem == "l":
                    print("moving left")
                    rv.left(95)
                    rv.forward(3)
                elif elem == "b":
                    print("moving backwards")
                    rv.backwards(3)
            n = input() #after every list of a commands, we need to listen again to insert more or just to type back
    if choice == "2":
        print("opening drawing...")
        print("available shapes: square, triangle, circle. Put the first letter")
        n = input()
        while n != "back":
            if n == "s":
                print("enter its width and height")
                w = int(input())
                h = int(input())
                for i in range(0, 2): #square have 4 sides - i enter 2 sides per turn. So 2*2=4!
                    rv.forward(h)
                    rv.right(90)
                    rv.forward(w)
                    rv.right(90)
                n = input()
            if n == "t":
                print("enter length of trinagle")
                l = int(input())
                for i in range(0, 3): #same as a triangle, but with one side per turn. 1 * 3 = 3!
                    rv.left(120)
                    rv.forward(l)
                n =input()
            if n == "c":
                print("sorry, but he left us:(") #Id love to add a circle, but rover doesnt have enough memory, so it impossiblle for him to processsuch hard figure
                #Otherwise, we need to use pretty hard algorithms
                n = "back"
    if choice = "3":
        print("entering avoider..")
        print("ready to start")
        while get_key() != "7": #get key just gives me sign then one button is pressed
            decision = randint(1, 2) #that random moment - we are choosing between 1 and 2
            obs = rv.rangermeasurement() #turn on sensors
            if ibs <= 0.1: #if sensors see something on a distance 0.1
                if decision == 1: #this if and else - is just different reaction on different results of randint
                    rv.stop()
                    rv.backwards(2)
                    rv.right(90)
                    rv.forward(100) #we can enter anything, but 100 is almost unreachible distance
                    # idea is that rover should go forward infinite amount of time, until he sees something
                    sleep(5)
                else:
                    rv.stop()
                    rv.backwards(2)
                    rv.left(90)
                    rv.forward(100)
                    sleep(5)
    if choice == "4":
        print("entering drift mode")
        while True: #just for fun - circling or drifting
            rv.left(360)
            sleep(2)
            rv.stop()
