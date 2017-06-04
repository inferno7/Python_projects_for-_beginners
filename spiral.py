from turtle import *
import colorsys

from random import randint

speed(5)# greater the magnitude slower is the pen  ..,  0- is the highest speed.

bgcolor('white') #background color

x = 1 #initialising x

while x < 400:  #looping 400 times
    r = randint(0, 255)  # makes variables r,g,b ( integer),to be randomly
    g = randint(0, 255)  # chosen between 0 and 255. It is changes every time
    b = randint(0, 255)  # the loop runs

    colormode(255)  # this is something that is irrelevant at this point
    # check the pythondocs link at the end for more info


    pencolor(r, g, b)  # changes the color of the pen to the rgb coordinates
    # obtained by the variables r, g, b changing each time

    fd(50 + x) #moving the pen forward
    rt(90.911)#moving the pen right

    x = x + 1 #incrementing x after every loop

exitonclick() # for showing the X option on the window


