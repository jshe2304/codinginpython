import turtle

# These are the variables you can experiment with. Change each variable and see how the drawing changes. 

my_background_color = 'black'

my_pen_color = 'white'

my_pen_size = 1

my_circle_size = 50

my_circle_closeness = 10

# This is the code. Look at it and see the variables we created above. 
# Excercise: Create a variable for turtle speed and put it into the code. 

turtle.bgcolor(my_background_color)
turtle.color(my_pen_color)
turtle.pensize(my_pen_size)
turtle.speed(20)

for i in range(75):
    turtle.circle(my_circle_size)
    turtle.left(my_circle_closeness)
