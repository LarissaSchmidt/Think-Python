import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

bob = turtle.Turtle()

polygon(bob, 6, 100)

turtle.mainloop()