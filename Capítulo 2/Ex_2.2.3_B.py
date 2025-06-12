import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from PIL import Image, ImageTk

passo_medio_calculado = None

def passo_medio_tempo_km(tempo_str):
    try:
        minutos, segundos = map(int, tempo_str.strip().split(':'))
        return timedelta(minutes = minutos, seconds = segundos)
    except ValueError as ve:
        messagebox.showerror('Formato de tempo inválido! Use mm:ss', f'Entrada inválida, tipo: {ve}') 

def calcular_chegada():
    try:
        hora_saida_str = entrada_hora_saida.get()
        hora_saida = datetime.strptime(hora_saida_str, '%H:%M')

        passo_str = entrada_passo_medio.get()
        passo_medio = passo_medio_tempo_km(passo_str)

        distancia_total = float(entrada_distancia_total.get().replace(',', '.'))
        if distancia_total < 0:
            raise ValueError('Distância não pode ser negativa! Insira a distância em km.')
        
        tempo_total = passo_medio * distancia_total
        hora_chegada = hora_saida + tempo_total
        hora_chegada_str = hora_chegada.strftime("%H:%M")

        messagebox.showinfo('Hora de Chegada',
                            f'Você chegará às {hora_chegada_str}.\n'
                            f'Tempo total estimado: {str(tempo_total)[:-3]}')
    except ValueError as ve:
        messagebox.showerror('Erro de entrada', f'Entrada inválida, tipo: {ve}')
    except Exception:
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos corretamente!')

janela = tk.Tk()
janela.title('Vou chegar para o café da manhã?')

imagem = Image.open(r'C:\Users\Usuario\Downloads\Think Python\cat.jpg')  
imagem = imagem.resize((300, 200))     
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janela, image = imagem_tk)
label_imagem.pack()

tk.Label(janela, text = 'Hora de Saída (HH:MM): ').pack()
entrada_hora_saida = tk.Entry(janela)
entrada_hora_saida.pack()

tk.Label(janela, text = 'Passo médio (mm:ss por km):').pack()
entrada_passo_medio = tk.Entry(janela)
entrada_passo_medio.pack()

tk.Label(janela, text = 'Distância total (km)').pack()
entrada_distancia_total = tk.Entry(janela)
entrada_distancia_total.pack()

botao = tk.Button(janela, text = 'Calcular', command = calcular_chegada)
botao.pack(pady=10)

janela.mainloop()