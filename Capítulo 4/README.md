# Capítulo 4: Estudo de caso: projeto de interface

Estamos observando como a biblioteca ```turtle``` se comporta e como podemos manusear ela. Brincando um pouco com o programa temos isso:

```ruby
import turtle
bob = turtle.Turtle()
print(bob)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.rt(90)
bob.fd(200)
bob.rt(90)
bob.fd(200)
bob.rt(90)
bob.fd(200)
bob.rt(90)
bob.fd(100)

turtle.mainloop()
```

*Resultado*

![image](https://github.com/user-attachments/assets/7faf1c25-d7c9-484e-ab5a-86809e981453)

Peguei umn código na internet que faz com que *bob* ande em um círculo, mostrando como podemos manusear essa biblioteca de diversas formas. 

```ruby
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
```

*Resultado*

![image](https://github.com/user-attachments/assets/ab39b59e-150f-4ccb-9793-2e74fc7a0817)

> **4.3 - Exercícios**

```1. Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado. Escreva uma chamada de função que passe bob como um argumento para o square e então execute o programa novamente.```

De maneira semelhante ao que fizemos anteriormente, criamos uma função que desenha um quadrado. A diferença é que, embora o resultado seja o mesmo, agora o código está organizado dentro de uma função reutilizável chamada ```square```, que recebe como parâmetro qualquer ```turtle``` e não apenas ```bob```. Isso torna o código mais modular e reutilizável, permitindo aplicar a mesma lógica a diferentes turtles em diferentes partes do programa.

```ruby
import turtle

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

bob = turtle.Turtle()
square(bob)

turtle.mainloop()
```

```2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o seu programa com uma variedade de valores para length.```

```ruby
import turtle

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

bob = turtle.Turtle()

square(bob, 50)

turtle.mainloop()
```

Funciona com qualquer valor de ```length```, quanto menor o valor menor o quadrado e vice versa.

```3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados. Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.```

```ruby
import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

bob = turtle.Turtle()

polygon(bob, 6, 100)

turtle.mainloop()
```

A função ```polygon``` recebe três parâmetros: a turtle ```t```, o número de lados ```n``` e o comprimento de cada lado ```length```. O valor de ```n``` define quantos lados o polígono terá, e o ângulo de virada é calculado como ```360 / n```, já que a soma dos ângulos exteriores de qualquer polígono regular é sempre 360 graus. Dentro da função, usamos um laço que se repete ```n``` vezes, fazendo a tartaruga avançar com ```forward(length)``` e depois virar para a esquerda com ```left(angle)```, formando assim os lados do polígono regular.

*Resultado*

![image](https://github.com/user-attachments/assets/96d1ac2e-fb37-4069-9ce0-25e18cf03c4b)

```4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.```


A função ```circle``` recebe como parâmetros uma turtle ```t``` e um raio ```r```, e tem como objetivo desenhar um círculo aproximado. Para isso, ela calcula a circunferência com a fórmula ```2 * π * r```, depois escolhe um número fixo de lados (como 50) para criar um polígono que se aproxime visualmente de um círculo. O comprimento de cada lado é obtido dividindo a circunferência pelo número de lados. Em seguida, ela chama a função ```polygon```, passando esses valores, para desenhar o círculo com base nessa aproximação. Ao testar com diferentes valores de ```r```, podemos observar a formação de círculos maiores ou menores, todos construídos com linhas pequenas que criam uma curva suave.



> **Exercício 4.1**
