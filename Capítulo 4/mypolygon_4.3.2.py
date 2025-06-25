import turtle

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

bob = turtle.Turtle()

square(bob, 50)

turtle.mainloop()