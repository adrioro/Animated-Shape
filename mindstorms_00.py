import turtle

window = turtle.Screen()
window.bgcolor("orange")
brad = turtle.Turtle()
brad.shape("arrow")
brad.color("lightblue")
brad.speed(9)
brad.pensize(5)

def draw_circle(): # Drawing a circle
    angie = turtle.Turtle()
    angie.shape ("arrow")
    angie.color("yellow")
    angie.circle(100)
    
    window.exitonclick()


def action(): # Function to be used in my loop
    brad.forward(100)
    brad.right(90)
    return
    

def draw_square(): # Drawing a square and triangle   
    max_times = 4
    times = 0
    
    while True:
        while times < 4:
            action()
            times = times +1
        else:
            while times < 3:
                action()
                times = times +1
            draw_circle()

draw_square()
