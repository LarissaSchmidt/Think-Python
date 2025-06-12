from datetime import datetime, timedelta

while True:
    try:
        print('\n--- Cálculo do Horário de Chegada após Corrida ---')

        # Entrada da hora de saída
        hora_saida_str = input('A que horas você saiu de casa? (formato HH:MM) ')
        hora_saida = datetime.strptime(hora_saida_str, "%H:%M")

        # Entrada do ritmo do passo mais lento
        print('\nInforme o ritmo (min e seg por quilômetro) do passo mais lento:')
        min_lento = int(input('Minutos: '))
        seg_lento = int(input('Segundos: '))
        if min_lento < 0 or seg_lento < 0 or seg_lento >= 60:
            raise ValueError("O tempo do passo mais lento deve ter minutos e segundos válidos.")

        # Entrada do ritmo do passo mais rápido
        print('\nInforme o ritmo (min e seg por quilômetro) do passo mais rápido:')
        min_rapido = int(input('Minutos: '))
        seg_rapido = int(input('Segundos: '))
        if min_rapido < 0 or seg_rapido < 0 or seg_rapido >= 60:
            raise ValueError("O tempo do passo mais rápido deve ter minutos e segundos válidos.")

        # Entrada das distâncias
        distancia_lenta = int(input('\nQuantos quilômetros serão percorridos no passo mais lento (total)? '))
        distancia_rapida = int(input('Quantos quilômetros serão percorridos no passo mais rápido? '))
        if distancia_lenta < 0 or distancia_rapida < 0:
            raise ValueError("As distâncias não podem ser negativas.")

        # Cálculo do tempo total
        passo_lento = min_lento * 60 + seg_lento
        passo_rapido = min_rapido * 60 + seg_rapido
        tempo_total_segundos = (distancia_lenta * passo_lento) + (distancia_rapida * passo_rapido)

        # Hora de chegada
        hora_chegada = hora_saida + timedelta(seconds=tempo_total_segundos)

        # Exibição dos resultados
        print(f'\nVocê saiu às {hora_saida.strftime("%H:%M")}.')
        print(f'O tempo total da corrida foi de {tempo_total_segundos // 60:.0f} minutos e {tempo_total_segundos % 60:.0f} segundos.')
        print(f'Você chegará em casa às {hora_chegada.strftime("%H:%M")} para o café da manhã.\n')

        break

    except ValueError as ve:
        print(f'\nErro: {ve}')
    except Exception:
        print('\nVocê digitou algo inválido. Tente novamente inserindo números válidos no formato correto.\n')