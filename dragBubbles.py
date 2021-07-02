#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:37:35 2020

@author: Dr. Z
Select a turtle - this code allows users to click and drag on a turtle.

YOU MUST USE ifClicked() and drag() together! Use the example to set up your code. Read comments for notes.
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

#======================== FUNCTIONS =======================

def ifClicked(x,y):
  """Determines which item in a list was clicked on based on location. Use with callback function for a screen:
    panel.onclick(ifClicked) or in conjunction with drag().
    Inputs:
      x - horizontal location of click event (automatically given if used with onclick function). (float or int)
      y - vertical location of click event (automatically given when used with onclick funciton). (float or int)
    Creates:
      the global variable selected which is the index of the bubble in the list that was clicked on. 
      Use selected to index lists (ex. someList[selected])"""
    
    global selected
    # call back function that selects clicked bubble
    for i in range(len(turtList)):
        # for every turtle in the list, get the position...
        currX = turtList[i].xcor()
        currY = turtList[i].ycor()
        
        # see if the click happened within a range of the position
        if round(currX)-30<=round(x)<=round(currX)+30 and round(currY)-30<=round(y)<=round(currY)+30:
            selected = i
            # print(selected) # uncomment to check which was selected
            break # stop stepping through the list if we got a hit
            
def drag(x,y): 
    """Correctly drags individual turtles in a list. Use in conjuction with ifClicked. You MUST use this code to stop backtracking glitch."""
    # from https://www.geeksforgeeks.org/turtle-ondrag-function-in-python/
    turtList[selected].ondrag(None) # clear the ondrag callback function (stops backtracking)
  
    #turtList[selected].setheading(turtle.towards(x, y)) # turn the turtle towards the mouse click
    turtList[selected].goto(x, y) # move the turtle to the position of the mouse pointer.
    turtList[selected].ondrag(drag) # return this function to the ondrag callback function
        
        
def wiggle(turtList,step=2):
    """step through all the bubbles in a list, and move them a bit. Works great with while loops!
    Inputs:
        turtList (required) - must be list of Turtle objects
        step (optional) - size of wiggle displacement in pixels (int)"""
    
    for i in range(len(turtList)):
        t = turtList[i] # pull out the turtle...
        t.goto(t.xcor()+random.randint(-step,step),t.ycor()+random.randint(-step,step))


#=====================INITIAL CONDITIONS=======================
panel.bgcolor('blue')

#Create a bunch of 5 randomly moving items (bubbles), using turtles
numBubbles = 5
turtList = [] # create an empty list

# Create list of turtles to act as bubbles
for i in range(numBubbles):
    turt = turtle.Turtle(shape='circle') #set our bubble shape
    turt.color('black','cyan') #set the color
    turt.up() #pick up the pen
    turt.shapesize(random.randint(3,5)) # make it a random size
    turt.goto(random.randint(100,500),random.randint(100,500)) # random start position
    turtList.append(turt) # add it to a list. 


step = 2 # amount of wiggle bubbles have
fps = 30 # frames per second
selected = 0    
T = 0

#=====================GAME LOOP=======================

while run:
    
    wiggle(turtList)
    
    # use these three lines for your drag code
    panel.onclick(ifClicked)
    thisBubble = turtList[selected]
    thisBubble.ondrag(drag)
    
    turtle.delay(fps) #set frame rate
    panel.update() # update the image with each "frame"

panel.mainloop()
        
