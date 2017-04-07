import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(9)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape ("arrow")
    angie.color("blue")
    angie.circle(100)
    
    window.exitonclick()


def action(): # Function to be used in my loop
    brad.forward(100)
    brad.right(90)
    return
    

def draw_square():    
    max_times = 4
    times = 0
    
    while True:
        while times < 4:
            action()
            times = times +1
        else:
            draw_circle()


        

        





draw_square()
