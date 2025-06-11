sim = ['s', 'sim', 'sm', 'claro']
nao = ['n', 'não', 'nao', 'no', 'na']

while True:
    print('\nVamos calcular quantos segundos, quantas milhas e qual o seu passo médio em uma corrida?!')
    print('\nDigite quanto tempo você fez de corrida:')
    while True:
        try: 
            horas = float(input('\nQuantas horas? '))
            minutos = float(input('Quantos minutos? '))
            segundos = float(input('Quantos segundos? '))

            r1 = horas * 60 * 60
            r2 = horas * 60
            r3 = minutos * 60
            r4 = segundos/60
            tempo_total_segundos = float(round(r1 + r3 + segundos, 2))
            print('\nNa sua corrida você fez um tempo total de:', tempo_total_segundos, 'segundos')
            break

        except ValueError:
            print('\nDigite apenas números!')

    print ('\nLegal, você correu muito!')

    while True:
        try: 
            km = float(input('\nAgora digite quantos km você percorreu na sua corrida: '))
            resultado_milhas = float(round(km / 1.61, 2))
            print('\nVocê correu:', resultado_milhas, 'milhas')
            break

        except ValueError:
            print('\nDigite apenas números!')
    
    print ('\nVamos descobrir qual o seu passo médio nessa corrida.')
    
    while True:
        resposta = input('\nVocê gostaria de usar os valores anteriores para descobrir o seu passo médio? (s/n) ').strip().lower()
        if resposta in sim:
            tempo = float(round(r2 + minutos + r4, 2))
            passo_milhas_tempo = round(resultado_milhas / tempo, 2)
            print (f'\nSeu passo médio é: {passo_milhas_tempo} milhas/minuto')
            exit()
        elif resposta in nao:
            while True:
                sair = input('\nVocê deseja sair do programa? ').strip().lower()
                if sair in sim:
                    print('\nOk, foi bom falar com você!')
                    exit()
                elif sair in nao:
                    break
                else:
                    print('\nDigite uma resposta válida.')
            break  
        else:
            print('\nDigite uma resposta válida.')  
    
                


