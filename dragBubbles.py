#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:37:35 2020

@author: Dr. Z
Select a turtle - this code allows users to click and drag on a turtle
"""


import random
import turtle 
turtle.colormode(255)
turtle.tracer(0) #turn off animation

#Create a panel to draw on. 
turtle.setup()
panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
#panel.setworldcoordinates(0, w, h, 0)

#========================MAKE VARIABLES=======================
panel.bgcolor('blue')

#Create a bunch of 5 randomly moving items (bubbles), using turtles
numBubbles = 5
turtList = [] # create an empty list


def ifClicked(x,y):
    global selected
    # call back function that selects clicked bubble
    for i in range(len(turtList)):
        currX = turtList[i].xcor()
        currY = turtList[i].ycor()
        if round(currX)-30<=round(x)<=round(currX)+30 and round(currY)-30<=round(y)<=round(currY)+30:
            selected = i
            print(len(turtList),selected)
            break
            
def drag(x,y): 
    """Correctly drags individual turtles in a list. Use in conjuction with ifClicked. You MUST use this code to stop backtracking glitch."""
    # from https://www.geeksforgeeks.org/turtle-ondrag-function-in-python/
    # stop backtracking
    turtList[selected].ondrag(None) 
  
    # move the turtle's angle and direction 
    # towards x and y
    #turtList[selected].setheading(turtle.towards(x, y))
    turtList[selected].goto(x, y)
    
    turtList[selected].ondrag(drag)
        
def delBubble(x,y):
    turtList[selected].ht() #hide the turtle to "delete" it
    #turtList.pop(selected)

# Create list of turtles to act as bubble items

for i in range(numBubbles):
    turt = turtle.Turtle(shape='circle') #set our bubble shape
    turt.color('black','cyan') #set the color
    turt.up() #pick up the pen
    turt.shapesize(random.randint(3,5)) # make it a random size
    turt.goto(random.randint(100,500),random.randint(100,500)) # random start position
    turtList.append(turt) # add it to a list. 


#=====================INITIAL CONDITIONS=======================
    
step = 2 # amount of wiggle bubbles have
fps = 30 # frames per second
selected = 0    
T = 0
run = True

#=====================GAME LOOP=======================

while run:
    T += 1
    
    # step through all the bubbles and move them a bit
    for i in range(len(turtList)):
        t = turtList[i] # pull out the turtle...
        t.goto(t.xcor()+random.randint(-step,step),t.ycor()+random.randint(-step,step))
    
    panel.onclick(ifClicked)
    thisBubble = turtList[selected]
    thisBubble.ondrag(drag)
    
#    if T >= 300:
#        run = False
    turtle.delay(fps) #set frame rate
    panel.update() # update the image with each "frame"

panel.mainloop()
        
