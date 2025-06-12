import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from PIL import Image, ImageTk

def parse_tempo(tempo_str):
    partes = list(map(int, tempo_str.strip().split(':')))
    if len(partes) == 2:
        minutos, segundos = partes
        return timedelta(minutes=minutos, seconds=segundos)
    elif len(partes) == 3:
        horas, minutos, segundos = partes
        return timedelta(hours=horas, minutes=minutos, seconds=segundos)
    else:
        raise ValueError('Formato de tempo inválido. Use mm:ss ou hh:mm:ss')

def calcular_passo_medio():
    try:
        tempo_total = parse_tempo(entrada_tempo_total.get())
        distancia = float(entrada_distancia_total.get().replace(',', '.'))
        if distancia <= 0:
            raise ValueError('Distância deve ser maior que zero.')
        passo_medio = tempo_total / distancia
        minutos = int(passo_medio.total_seconds() // 60)
        segundos = int(passo_medio.total_seconds() % 60)
        passo_formatado = f"{minutos:02}:{segundos:02}"
        entrada_passo_medio.delete(0, tk.END)
        entrada_passo_medio.insert(0, passo_formatado)
        janela_calculo.destroy()
    except Exception as e:
        messagebox.showerror('Erro no cálculo do passo médio', str(e))

def abrir_janela_calculo_passo():
    global janela_calculo, entrada_tempo_total, entrada_distancia_total
    janela_calculo = tk.Toplevel()
    janela_calculo.title('Calcular Passo Médio')

    tk.Label(janela_calculo, text='Tempo total da corrida (mm:ss ou hh:mm:ss):').pack()
    entrada_tempo_total = tk.Entry(janela_calculo)
    entrada_tempo_total.pack()

    tk.Label(janela_calculo, text='Distância percorrida (km):').pack()
    entrada_distancia_total = tk.Entry(janela_calculo)
    entrada_distancia_total.pack()

    tk.Button(janela_calculo, text='Calcular Passo Médio', command=calcular_passo_medio).pack(pady=5)

def parse_tempo_por_km(tempo_str):
    try:
        minutos, segundos = map(int, tempo_str.strip().split(':'))
        return timedelta(minutes=minutos, seconds=segundos)
    except:
        raise ValueError('Formato de tempo inválido! Use mm:ss')

def calcular_chegada():
    try:
        hora_saida_str = entrada_hora_saida.get()
        hora_saida = datetime.strptime(hora_saida_str, '%H:%M')

        passo_str = entrada_passo_medio.get()
        passo_medio = parse_tempo_por_km(passo_str)

        dist_total = float(entrada_dist_total.get().replace(',', '.'))
        if dist_total < 0:
            raise ValueError('Distância não pode ser negativa!')

        tempo_total = passo_medio * dist_total
        hora_chegada = hora_saida + tempo_total
        hora_chegada_str = hora_chegada.strftime('%H:%M')

        messagebox.showinfo('Hora de Chegada',
                            f'Você chegará às {hora_chegada_str}.\n'
                            f'Tempo total estimado: {str(tempo_total)[:-3]}')

    except ValueError as ve:
        messagebox.showerror('Erro de entrada', f'Entrada inválida: {ve}')
    except Exception as e:
        messagebox.showerror('Erro', f'Por favor, preencha todos os campos corretamente!\n{e}')

def iniciar_janela_principal():
    global entrada_hora_saida, entrada_distancia, entrada_passo_medio, janela  # Declare globais
    janela = tk.Tk()
    janela.title('Vou chegar para o café da manhã?')

    # Carregar imagem aqui dentro
    imagem = Image.open(r'C:\Users\Usuario\Downloads\Think Python\cat.jpg')
    imagem = imagem.resize((300, 200))
    imagem_tk = ImageTk.PhotoImage(imagem)
    
    # Guardar referência para não ser apagada
    janela.imagem_tk = imagem_tk

    label_imagem = tk.Label(janela, image=imagem_tk)
    label_imagem.pack()

    # Resto dos widgets
    tk.Label(janela, text='Hora de Saída (HH:MM): ').pack()
    entrada_hora_saida = tk.Entry(janela)
    entrada_hora_saida.pack()

    tk.Label(janela, text='Distância Total (km): ').pack()
    entrada_distancia = tk.Entry(janela)
    entrada_distancia.pack()

    tk.Label(janela, text='Passo Médio (MM:SS por km): ').pack()
    entrada_passo_medio = tk.Entry(janela)
    entrada_passo_medio.pack()

    botao = tk.Button(janela, text='Calcular Chegada', command=calcular_chegada)
    botao.pack()

    janela.mainloop()

def pergunta_inicial():
    resposta = messagebox.askyesno('Passo Médio', 'Você quer que o programa calcule o seu passo médio?')
    if resposta:
        abrir_janela_calculo_passo()
    iniciar_janela_principal()

# Janela inicial de decisão
root = tk.Tk()
root.withdraw()
pergunta_inicial()