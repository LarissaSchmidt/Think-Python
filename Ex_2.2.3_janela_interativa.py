import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calcular_chegada():
    try:
        hora_saida_str = entrada_hora_saida.get()
        hora_saida = datetime.strptime(hora_saida_str, '%H:%M')

        duracao_str = entrada_duracao.get()
        horas, minutos = map(int, duracao_str.split(':'))
        duracao = timedelta(hours=horas, minutes=minutos)

        hora_chegada = hora_saida + duracao
        hora_chegada_str = hora_chegada.strftime("%H:%M")

        messagebox.showinfo('Hora de Chegada', f'Você chegará às {hora_chegada_str}.')

    except ValueError as ve:
        messagebox.showerror('Erro de entrada', f'Entrada inválida, tipo: {ve}')

    except Exception:
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos corretamente!')


janela = tk.Tk()

janela.title('Vou chegar para o café da manhã?')

tk.Label(janela, text = 'Hora de Saída (HH:MM): ').pack()
entrada_hora_saida = tk.Entry(janela)
entrada_hora_saida.pack()

tk.Label(janela, text = 'Duração da Viagem (HH:MM)').pack()
entrada_duracao = tk.Entry(janela)
entrada_duracao.pack()

botao = tk.Button(janela, text = 'Calcular', command = calcular_chegada)
botao.pack()












janela.mainloop()

