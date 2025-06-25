import turtle
import math

def polygon(t, n, length):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

if __name__ == '__main__':
    bob = turtle.Turtle()
    circle(bob, 100)
    turtle.done()