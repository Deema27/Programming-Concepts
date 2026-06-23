''' Description:
Simulates a race between a tortoise and a hare
using the turtle graphics module and random movement.'''

import turtle
import random

#Function to update the tortoise's position
def track_tortoise_position(t_position):

    #Generate a random number between 1 and 10
    num = random.randint(1, 10)

    #Move tortoise forward by 3 spaces
    if 1 <= num <= 5:
        t_position += 3

    #Move tortoise backward by 5 spaces
    elif 6 <= num <= 7:
        t_position -= 5

    #Move tortoise forward by 1 space
    elif 8 <= num <= 10:
        t_position += 1

    #Prevent tortoise from moving past the starting line
    if t_position < -100:
        t_position = -100

    #Prevent tortoise from moving past the finish line
    elif t_position > 100:
        t_position = 100

    #Return updated position
    return t_position


#Function to update the hare's position
def track_hare_position(h_position):

    #Generate a random number between 1 and 10
    num1 = random.randint(1, 10)

    #Hare sleeps and does not move
    if 1 <= num1 <= 2:
        pass

    #Hare makes a big hop forward
    elif 3 <= num1 <= 4:
        h_position += 7

    #Hare makes a small hop forward
    elif 5 <= num1 <= 7:
        h_position += 1

    #Hare slips backward slightly
    elif 8 <= num1 <= 9:
        h_position -= 2

    #Hare slips backward greatly
    elif num1 == 10:
        h_position -= 10

    #Prevent hare from moving past the starting line
    if h_position < -100:
        h_position = -100

    #Prevent hare from moving past the finish line
    elif h_position > 100:
        h_position = 100

    #Return updated position
    return h_position


#Create the turtle graphics screen
screen = turtle.Screen()

#Set window title
screen.title("Tortoise V.S. Hare!")

#Set background color
screen.bgcolor("pink")


#Create turtle objects
tortoise = turtle.Turtle()
hare = turtle.Turtle()
finish_line = turtle.Turtle()
start_line = turtle.Turtle()
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()
pen4 = turtle.Turtle()


#Customize tortoise appearance
tortoise.shape("turtle")
tortoise.color("green")

#Customize hare appearance
hare.shape("turtle")
hare.color("white")


#Hide drawing turtles
finish_line.hideturtle()
start_line.hideturtle()
pen1.hideturtle()
pen2.hideturtle()
pen3.hideturtle()
pen4.hideturtle()


#Draw the starting line
start_line.penup()
start_line.setpos(-100, 0)
start_line.pendown()
start_line.left(90)
start_line.forward(50)

#Draw the finish line
finish_line.penup()
finish_line.setpos(100, 0)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(50)


#Write "Start" label
pen1.penup()
pen1.setpos(-100, 50)
pen1.write("Start")

#Write "End" label
pen2.penup()
pen2.setpos(100, 50)
pen2.write("End")


#Set initial tortoise position
tortoise.penup()
tortoise.setpos(-100, 0)

#Set initial hare position
hare.penup()
hare.setpos(-100, 50)


#Store starting positions
tortoise_position = -100
hare_position = -100

#Initialize race timer
race_clock = 0


#Continue race until one racer reaches the finish line
while tortoise_position < 100 and hare_position < 100:

    #Increase race timer
    race_clock += 1

    #Update racer positions
    tortoise_position = track_tortoise_position(tortoise_position)
    hare_position = track_hare_position(hare_position)

    #Move tortoise turtle
    tortoise.penup()
    tortoise.setpos(tortoise_position, 0)
    tortoise.pendown()

    #Move hare turtle
    hare.penup()
    hare.setpos(hare_position, 50)
    hare.pendown()


#Determine the winner
if hare_position > tortoise_position:
    winner = "Hare"

elif tortoise_position >= hare_position:
    winner = "Tortoise"


#Display winner message
pen3.penup()
pen3.setpos(103, 20)
pen3.write(f'{winner} wins!')

#Display race time
pen4.penup()
pen4.setpos(80, -60)
pen4.write(f'Time of race: {race_clock} seconds.')


#Keep turtle graphics window open
turtle.done()
