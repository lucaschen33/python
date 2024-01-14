import turtle
import math

factor = 1

def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b
#Square color
    x.pencolor("blue")
#Creating the first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
#Continuing the sequence
    temp = square_b
    square_b = square_b + square_a
    square_a = temp
#Creating the rest of the squares for how many squares the user would like
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        
        temp = square_b
        square_b = square_b + square_a
        square_a = temp
#Moving the small cursor like shape to the middle of the sequence
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
#Making the Spiral Color Red
    x.pencolor("red")
#Making the Spiral
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b
#Asking the user how many time they would like to zoom into the sequence
def change_scale():
    global factor
    while True:
        try:
            scale = float(input('Enter the zoom factor (must be a positive number): '))
#Making sure the user inputs an integer greater than 0
            if scale <= 0:
                print("Please enter a number that is greater than 0.")
            else:
                factor = scale
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
#Asking the user how many iterations they would like to make
while True:
    try:
        n = int(input('Enter the number of iterations (must be > 1): '))
#Making sure the user inputs an integer that's greater than 1
        if n <= 1:
            print("Please enter a number that is greater than 1.")
        else:
#Running the program with the given information and also printing the inputed number for the user.
            print("Fibonacci series for", n, "elements :")
            x = turtle.Turtle()
            x.speed(100)
            change_scale()
            fiboPlot(n)
            turtle.done()
            break
    except ValueError:
        print("Invalid input! Please enter an integer.")