#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:37:35 2020

@author: Dr. Z
@author: YOUR NAME

DELETE this line for full credit - this script, as-is, blinks a turtle on blue backgnd to show framerate

***DESCRIPTION: What does your game do? What is the goal? How do you know when you win or lose?***
"""


import random, turtle
turtle.colormode(255)

#Create a panel to draw on. 
turtle.setup()
panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#========================MAKE GLOBAL VARIABLES=======================
example = turtle.Turtle("circle")


#==========================DEFINE FUNCTIONS===========================


#===============INITIAL CONDITIONS & LOCAL VARIABLES==================
panel.bgcolor('blue')

# Define your start variables here!
fps = 100 # framerate for animation
run = True

#=======================GAME LOOP (Execution)=========================

while run:

    # Add your game activity here
    if example.isvisible():
        example.ht()  # hide the turtle if it's showing
    else:
        example.st() # show the turtle if it's hidden
    
    #if <END CONDITION>:
    #   run = False
    
    turtle.delay(fps) #set frame rate
    panel.update() # update the image with each "frame"

panel.mainloop() # keep listeners on for mouse press
turtle.done()
        