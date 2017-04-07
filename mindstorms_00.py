
import turtle

window = turtle.Screen()
window.bgcolor("orange")
brad = turtle.Turtle()
brad.shape("arrow")
brad.color("lightblue")
brad.speed(9)
brad.pensize(5)

def draw_circle(): # Function to draw a circle
    angie = turtle.Turtle()
    angie.shape ("arrow")
    angie.color("yellow")
    angie.circle(50)
    angie.color("red")
    angie.pensize(5)
    angie.circle(100)
    window.exitonclick()

def action(): # Action to be used in my draw_square loop
    brad.forward(100)
    brad.right(90)
    return

def action_t(): # Action to be used in my draw_triangle loop
    brad.forward(100)
    brad.right(120)
    return

def draw_triangle(): # Drawing a triangle
    brad.pensize(11)
    brad.color("white")
    max_times = 3
    times = 0
    while times < 3:
        action_t()
        times = times +1
    else:
        draw_circle()

    

def draw_square(): # Drawing a square and circle   
    max_times = 4
    times = 0    
    while True:
        while times < 4:
            action()
            times = times +1
        else:
            draw_triangle()
            

draw_square()
