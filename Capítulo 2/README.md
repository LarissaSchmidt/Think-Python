# Capítulo 2: Variáveis, expressões e instruções

> **Exercício 2.1**

No Python a variável que guarda uma informação não pode ser numérica, quando estamos fazendo ```n = 42``` estamos dizendo ao programa *n* recebe *42*. Podemos atribuir um mesmo valor para variáveis de nome diferentes como ```x = y = 1```.

```ruby
#42 = n da erro, número não guarda informação, não pode ser uma variável que recebe info
n = 42
print(n)

#Podemos atribuir um mesmo valor para variáveis de nome diferentes
x = y = 1
print(x)
print(y)
print(x+y)
```
*Resultado* 
```
42
1
1
2
```

Apesar de ser possível utilizar o ; para separar variáveis, idealmente utiliza-se uma nova linha para cada informação adicionada. O ; só é usado se você quiser escrever duas instruções na mesma linha. Já o ponto não deve ser utilizado, pois ele é utilizado em Python para acessar partes de algo, como deixar todas as letras de um input em caixa alta.

```ruby
#x = 5; y = 10 pode ser utilizado, mas usualmente usamos a separação em linhas
x = 5
y = 10
print(x+y)

#Exemplo de utilização de .upper()
nome = input('Qual o seu nome? ')
nome_maiusculo = nome.upper()
print(f'Olá {nome_maiusculo}!')

#Para multiplicar algo você precisa utilizar o operador *, sem ele o programa identificara xy como variável
print(x*y)
```
*Resultado* 
```
15
Input do usuário --> Olá INPUT DO USUÁRIO!
50
```

> **Exercício 2.2**

```1. O volume de uma esfera com raio r```$V = \frac{4}{3} \pi r^3$```. Qual é o volume de uma esfera com raio 5?```

Criei um programa simples e reutilizável para calcular o volume de esferas a partir do raio informado pelo usuário. 

Importei a biblioteca de matemática com ```import math``` para acessar o valor de ```pi```, essencial na fórmula do volume de uma esfera. Também me atentei à apresentação do resultado, que é exibido já com duas casas decimais, utilizando ```:.2f``` para formatar o número do tipo ```float```.

```ruby
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
```

```2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?```

Ao invés de resolver a questão apenas com os valores fixos fornecidos, optei por criar um programa reutilizável, no qual a livraria possa inserir diferentes preços, descontos e quantidades conforme a necessidade.

Utilizei de variáveis para armazenar as informações fornecidas e um laço ```while True``` para manter o programa em execução até que o usuário insera valores válidos. Usei o bloco ```try/except``` para tratar os possíveis erros de entrada. As entradas são recebidas com ```input()```, e o tipo de dado escolhido é importante: por exemplo, a variável ```quantidade_atacado```  deve ser um número inteiro ```int()``` , já que não faz sentido pedir, por exemplo, 2,5 livros. Por outro lado, para variáveis como  ```preco_livro``` e ```desconto```, utilizei ```float()``` para permitir valores decimais. 

O programa realiza todos os cálculos automaticamente e informa o custo total da compra com base nos dados inseridos, funcionando para qualquer tipo de venda que a livraria deseje simular.

```ruby
frete_fixo = 3
frete_adicional = 0.75

while True:
    try:
        preco_livro = float(input('Qual o preço do livro? R$'))
        desconto = float(input('Quantos % de desconto a livraria ganha nessa compra? (ex: 20 para 20%) '))
        quantidade_atacado = int(input('Quantas unidades serão pedidas? '))
        
        porcentagem = float(desconto)/100
        preco_com_desconto = (preco_livro * quantidade_atacado) * (1 - porcentagem)
        frete_total = frete_fixo + ((quantidade_atacado - 1) * frete_adicional)
        custo_total = frete_total + preco_com_desconto

        if quantidade_atacado > 1:
            print(f'\nSabemos que o valor do frete é R${frete_fixo} mais R${frete_adicional} por exemplar. O frete total para essa compra é R${frete_total}')
            print(f'\nO custo total dessa compra é R${custo_total}')
            break
        elif quantidade_atacado == 1:
            print(f'O valor total do frete é R${frete_fixo}')
            print(f'O valor total da compra é R${preco_livro+frete_fixo}')
            break
        else:
            print('Esse não é um valor válido de unidades')
    except Exception:
        print('\nVocê precisa digitar um número válido.')
```

```3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?```


Resolvi testar a criação de uma interface gráfica para que o usuário interaja diretamente em uma janela separada, e não no terminal. Importei a biblioteca gráfica ```tkinter``` e a apelidei de ```tk``` para facilitar o uso dos comandos ao longo do código. Criei a janela principal com ```janela = tk.Tk()```, nomeando-a com ```janela.title()```. Para mantê-la aberta e responsiva, utilizei o ```janela.mainloop()```.

```ruby
import tkinter as tk

janela = tk.Tk()

janela.title('Vou chegar para o café da manhã?')

janela.mainloop()
```
![image](https://github.com/user-attachments/assets/0561870a-e315-46e3-99ef-7bc3ed4c854d)

Alguns componentes essenciais para que o programa funcione são: campos de entrada, rótulos, botões e uma área que mostre o resultado. 

Utilizei também o ```from tkinter import messagebox``` para ter acesso a uma função que permite exibir janelas de aviso — úteis para mostrar mensagens de erro ou confirmação ao usuário.

Além disso, importei ```datetime``` e ```timedelta``` da biblioteca ```datetime```, que são funções específicas para trabalhar com data e hora no Python. Elas permitem calcular prazos, datas futuras, comparar horários com precisão e até descobrir que horas o usuário chegaria em casa depois de uma corrida matinal.
 
 ```ruby
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

janela = tk.Tk()

janela.title('Vou chegar para o café da manhã?')

janela.mainloop()
```

Aqui já temos a janela principal pronta para receber os dados do programa. Para isso defini a ideia central que é permitir que o usuário preencha informações sobre uma corrida. Incluindo horário de saída, ritmos em diferentes trechos e a distância percorrida. A partir dessas informações o programa deve calcular o horário de chegada. 

Primeiro deve-se define tudo o que vai ser usado, depois monta-se o que será exibido ou executado. Para isso defini uma função ```def``` chamada ```calcular_chegada()```. Essa função deverá ser executada toda vez que o usuário clicar em um botão de calcular, que será codado logo adiante. Utilizei tudo que já foi aplicado nos exercícios anteriores como o tratamento de erros com ```try``` e ```except```.

```ruby
def calcular_chegada():
    try:
        hora_saida_str = entrada_hora_saida.get()
```

A váriavel ```hora_saida_str``` irá armazenar a resposta do usuário em um campo de entrada da interface. O ```.get()```é um widget de entrada do ```tkinter``` que lê esse o valor de resposta digitado pelo usuário. 
Isso nos retorna uma *string*, mas para tratar essa informação como hora e data devemos mudar o *tipo* dela e transforma-la em um *objeto*. 

```ruby
def calcular_chegada():
    try:
        hora_saida_str = entrada_hora_saida.get()
        hora_saida = datetime.strptime(hora_saida_str, '%H:%M')
```

A função ```datetime.strptime()``` converte a *string* recebida do usuário para um objeto do tipo ```datetime```. O formato esperado para esse objeto é definido então com o argumento ```'%H:%M'```. Nesse caso sendo ```%H``` formato de 24horas e ```%M``` formato para minutos. Se o usuário digitar algo como *14:30* então a ```hora_saida``` será correspondente a *14 horas e 30 minutos*. 

Agora precisamos saber o tempo de duração da caminhada da pessoa. Assim iremos utilizar o mesmo racíocinio e fazer uma função ```duracao_caminhada``` e transformar o valor de saída em um objeto. 

```ruby
        duracao_caminhada_str = entrada_duracao.get()
        horas, minutos = map(int, duracao_caminhada_str.split(':'))
```

A função ```.split(':')``` divide a string em dois pedaços onde houver *:*, no caso quando a pessoa digitar que ela caminhou durante '02:35' (duas horas e trinta e cinco minutos) esse valor irá ser transformado em uma lista ['02,'35']. Mesmo que tenhamos essa lista, os valores ainda são *strings*, para transformarmos eles em números inteiros utilizamos a função ```map(int, )``` resultando em ```horas = 2``` e ```minutos = 15```.

No Python para somar um tempo a um instante específico precisamos utilizar dois operadores: ```datetime``` que representa um instante completo no tempo (data + hora) e ```timedelta``` que representa uma duração (ex: 1 hora e 15 minutos), não utilizamos dois ```datetime``` mesmo que possa até funcionar em termos de horário, mas ao somar dois datetimes pode-se levantar exceções e possibilidade de erros. 

```ruby
        duracao_caminhada_str = entrada_duracao.get()
        horas, minutos = map(int, duracao_caminhada_str.split(':'))
        duracao_caminhada = timedelta(hours=horas, minutes=minutos)
```

Podemos finalmente somar o horário de saída ```hora_saida``` do tipo ```datetime``` com o tempo de duração ```duracao```do tipo ```timedelta```, resultando no horário de chegada ```hora_chegada``` do tipo ```datetime```.

```ruby
        hora_chegada = hora_saida + duracao
        hora_chegada_str = hora_chegada.strftime("%H:%M")
```

Para mostrar isso ao usuário formatamos o datetime da hora de chegada para uma *string* também no formato de 24horas. Para transformar um valor do tipo ```datetime``` para *string*, utilizamos ```strftime```. E fazemos com que uma mensagem seja mostrada na janela com ```messagebox```.

```ruby
        messagebox.showinfo('Hora de Chegada', f'Você chegará às {hora_chegada_str}.')
```

Essa caixa de informação terá o título de *'Hora de Chegada'* e o resultado será exibido onde está ```{hora_chegada_str}```.

Para fechar a função ```try``` adicionamos um ```except``` que também contará com uma ```messagebox```, para informar ao usuário qual foi o erro que ele cometeu ao preencher os valores.

```ruby
 except ValueError as ve:
        messagebox.showerror('Erro de entrada', f'Entrada inválida, tipo: {ve}')
```
![image](https://github.com/user-attachments/assets/a7e3c025-eb6d-48a6-b4af-66e578316b07)

Finalizamos a etapa de definição da função e agora podemos avançar para a construção da interface gráfica. Por uma questão de capricho, decidi adicionar uma imagem à janela, tornando a interface mais amigável. Para isso, foi necessário importar uma biblioteca capaz de manipular imagens.

```ruby
from PIL import Image, ImageTk
```

Com ela podemos selecionar o caminho da imagem e adicionar isso ao nosso programa. A função ```Image.open('')``` abre o arquivo de imagem no caminho especificado em *''*, a letra *r* indica que é uma *raw string* e isso é necessário para que o programa possa ignorar os caracteres especiais como a contra barra *\*.

```ruby
imagem = Image.open(r'C:\Users\Usuario\Downloads\Think Python\cat.jpg')  
imagem = imagem.resize((300, 200))     
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.pack()
```
A função ```.resize((300, 200))``` redimensiona a imagem para 300pixels de largura e 200 de altura, por exemplo. Esses valores podem ser ajustados conforme necessário para evitar distorções na imagem.

Em seguida, a função ```ImageTk.PhotoImage(imagem)``` converte a imagem no formato ```PIL``` para um formato compatível com o ```tkinter```, que aceita apenas imagens nos formatos ```PhotoImage``` ou ```BitmapImage```. Para exibir a imagem na interface, criamos um rótulo (label) e o associamos à imagem convertida. Isso é feito com a instrução ```label_imagem = tk.Label(janela, image = imagem_tk)```. Por fim, utilizamos o método ```.pack()``` para inserir o rótulo na janela, garantindo que a imagem apareça no layout da interface.

![image](https://github.com/user-attachments/assets/0d51e442-030a-4ff1-92ee-4cacf9fa76e8)

Criamos um rótulo com o texto ```'Hora de Saída (HH:MM):'``` utilizando ```tk.Label```, que é inserido na janela com o método ```.pack()```. Logo abaixo, adicionamos um campo de entrada com ```tk.Entry(janela)``` para que o usuário possa digitar o horário desejado, também posicionado com ```.pack()```.

Em seguida, repetimos o mesmo processo para solicitar a duração da viagem. Criamos um novo rótulo com o texto ```'Duração da Viagem (HH:MM)'``` e um novo campo de entrada logo abaixo para que o usuário insira esse valor.

Por fim, adicionamos um botão com o texto ```'Calcular'``` utilizando ```tk.Button```. Esse botão é vinculado à função ```calcular_chegada``` por meio do parâmetro ```command```, ao ser clicado ele executará essa função. O botão também é posicionado na interface com o método ```.pack()```.

```ruby
tk.Label(janela, text = 'Hora de Saída (HH:MM): ').pack()
entrada_hora_saida = tk.Entry(janela)
entrada_hora_saida.pack()

tk.Label(janela, text = 'Duração da Viagem (HH:MM)').pack()
entrada_duracao = tk.Entry(janela)
entrada_duracao.pack()

botao = tk.Button(janela, text = 'Calcular', command = calcular_chegada)
botao.pack()
```

![image](https://github.com/user-attachments/assets/f69a797d-8e0c-42b5-9225-5c786ef19361)

No total temos esse código:

```ruby
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from PIL import Image, ImageTk

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

imagem = Image.open(r'C:\Users\Usuario\Downloads\Think Python\cat.jpg')  
imagem = imagem.resize((300, 200))     
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janela, image = imagem_tk)
label_imagem.pack()

tk.Label(janela, text = 'Hora de Saída (HH:MM): ').pack()
entrada_hora_saida = tk.Entry(janela)
entrada_hora_saida.pack()

tk.Label(janela, text = 'Duração da Viagem (HH:MM)').pack()
entrada_duracao = tk.Entry(janela)
entrada_duracao.pack()

botao = tk.Button(janela, text = 'Calcular', command = calcular_chegada)
botao.pack()

janela.mainloop()
```
