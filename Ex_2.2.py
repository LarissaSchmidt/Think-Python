import math

while True:
    try:
        print('\nVamos calcular o volume de esferas para você!')

        raio = float(input('\nDigite o raio da esfera: '))

        volume = (4/3) * math.pi * (raio ** 3)

        print(f'O volume da esfera com raio {raio} é {volume:.2f}')
        exit()
    except Exception:
        print('\nDigite apenas números!')