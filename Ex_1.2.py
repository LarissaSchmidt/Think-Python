#Exercício 2.2
#1)

print('Quantos segundos tem no tempo que você quer descobrir?')

while True:
    try: 
        horas = int(input('Quantas horas? '))
        minutos = int(input('Quantos minutos? '))
        segundos = int(input('Quantos segundos? '))

        r1 = horas * 60 * 60
        r2 = minutos * 60
        resultado = r1 + r2 + segundos
        print('Resultado:', resultado, 'segundos')
        break

    except ValueError:
        print('Digite apenas números inteiros!')

#2)

while True:
    try: 
        km = float(input('Quantos km você quer converter para milhas? '))
        resultado_milhas = round(km / 1.61, 2)
        print('Resultado:', resultado_milhas, 'milhas')
        break

    except ValueError:
        print('Digite apenas números que façam sentido para km!')