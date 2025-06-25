import turtle
import math

# Reutilizando a função polygon
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

# Função circle: aproxima um círculo usando um polígono de muitos lados
def circle(t, r):
    circumference = 2 * math.pi * r     # fórmula da circunferência
    n = 50                               # número de lados para suavidade
    length = circumference / n          # comprimento de cada lado
    polygon(t, n, length)

# Testando com diferentes raios
bob = turtle.Turtle()
circle(bob, 50)     # círculo com raio 50
bob.penup()
bob.goto(150, 0)
bob.pendown()
circle(bob, 100)    # círculo com raio 100
bob.penup()
bob.goto(-150, 0)
bob.pendown()
circle(bob, 30)     # círculo com raio 30

turtle.mainloop()