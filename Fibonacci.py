import turtle
import math

factor = 1

def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b
    x.pencolor("blue")

    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    temp = square_b
    square_b = square_b + square_a
    square_a = temp
    
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

    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
    x.pencolor("red")

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

def change_scale():
    global factor
    while True:
        try:
            scale = float(input('Enter the zoom factor (must be a positive number): '))
            if scale <= 0:
                print("Please enter a number that is greater than 0.")
            else:
                factor = scale
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    try:
        n = int(input('Enter the number of iterations (must be > 1): '))
        if n <= 1:
            print("Please enter a number that is greater than 1.")
        else:
            print("Fibonacci series for", n, "elements :")
            x = turtle.Turtle()
            x.speed(100)
            change_scale()
            fiboPlot(n)
            turtle.done()
            break
    except ValueError:
        print("Invalid input! Please enter an integer.")
