"""
Simple coundtown timer using turtle. This timer is set to countdown from 30, updates once a second. Prints text on screen.
Modified from: https://www.codetoday.co.uk/post/creating-a-simple-timer-in-python-and-using-it-with-programs-in-turtle

THIS IS OUTSIDE CODE. IT MUST BE CITED
"""
import time
import turtle

window = turtle.Screen()
window.tracer(0) # turn off turtle's built-in animation

player = turtle.Turtle()
timer_text = turtle.Turtle()

duration = 30
start = time.time()

# use this while loop as your animation/game loop
while time.time() - start < duration:
  
    # example animation. Delete next two lines and replace with your code
    player.forward(1)
    player.left(1)
    
    # timer animation. Keep the next two lines to keep the timer.
    timer_text.clear() # this will ONLY clear the timer
    timer_text.write(int(time.time() - start), font=("Courier", 30)) # write the time left on the screen, whole seconds only

    # you probably don't want change the code below this line
    window.update() #update the animation

turtle.done()
