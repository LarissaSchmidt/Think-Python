# Think Python - How To Like a Computer Scientist
<img src="https://howtolearnmachinelearning.com/wp-content/uploads/2020/11/Think_Python.png" width="400">

# Capítulo 1: A jornada do programa

**Glossário:**
```
int – número inteiro (ex: 1, 42, -7)

float – número decimal ou quebrado (ex: 3.14, -0.5)

str – string, sequência de caracteres ou texto (ex: 'olá', 'python')

print – função que exibe algo na tela

input – função que recebe uma entrada do usuário

bug – erro ou falha no código

debugging – processo de encontrar e corrigir bugs

operator – símbolo que realiza uma operação (ex: +, -, *, /)

expression – combinação de valores e operadores que Python pode avaliar (ex: 2 + 3)

statement – instrução completa que o Python executa (ex: print("oi"))

variable – nome que armazena um valor (ex: x = 5)

assignment – ação de atribuir um valor a uma variável (ex: x = 10)

value – dado armazenado ou manipulado pelo programa (ex: 42, "texto")

type – tipo de dado (ex: int, float, str)

syntax – conjunto de regras para escrever o código corretamente

comment – texto no código ignorado pelo Python, usado para explicações (# isso é um comentário)

function – bloco de código reutilizável que realiza uma tarefa (ex: print())

parameter – valor passado para uma função

return – valor que uma função devolve após executar

prompt – mensagem exibida para o usuário durante a entrada de dados (ex: input('Digite seu nome: '))

^ – operador bitwise XOR (exclusive or) que compara bits (não muito usado no começo, mas aparece)
```

> **Exercício 1.1**

No exercício, o comando ```print('Hello, World!')``` imprime a frase **Hello, World!** na tela, mostrando uma mensagem para o usuário.

```ruby
print ('Hello, World!')

print (2+2)
```
*Resultado* 
```
Hello, World!
4
```

O Python interpreta o ++ como um sinal positivo extra: 2+(+2). O Python não aceita números com zero a esquerda, ou seja, que iniciam com um zero, como exemplo 02. Para utilizar essa notação, deve-se transforma o valor em uma string:

```ruby
print (2++2)
#identifica como incremento como se fosse 2 + (+2)

print ('02')
#02 não é aceito pela notação do 0 a esquerda, para utilizar isso tranformar em string
```
*Resultado* 
```
4
02
```

Utilizei uma função definindo uma variável ```palavra``` e coloquei dentro dela o número 2.

```ruby
palavra = 2
print (palavra)
#palavra se torna uma variável
```
*Resultado* ```2```

> **Exercício 1.2**

```1. Quantos segundos há em 42 minutos e 42 segundos?```

Escolhi fazer um código que possa descobrir quantos segundos existem em um tempo informado pelo usuário (em horas, minutos e segundos). Primeiro, ele mostra uma mensagem com o **print**, perguntando o que o usuário quer descobrir. 

Depois, ele entra em um laço **while**, que faz o programa repetir até que tudo seja digitado corretamente. Dentro do laço, ele usa o **input** para perguntar quantas horas, minutos e segundos o usuário quer converter, e o **int** serve para transformar essas respostas em números inteiros. 

O programa então faz as contas: multiplica as horas por 3600 (porque cada hora tem 3600 segundos) e os minutos por 60, e soma tudo com os segundos. 

O resultado é exibido com outro **print**. Se o usuário digitar algo errado (como letras ou símbolos), o **try**/**except** impede que o programa quebre e mostra uma mensagem de erro dizendo para digitar apenas números.

```ruby
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
```

```2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.```

Utilizei o mesmo raciocínio para esse código. Note que ele usa o número 1.61 como fator de conversão (1 milha = 1,61 km). 

O valor digitado pelo usuário é transformado em **float**, ou seja, permite números com vírgula (como 12.5 km, por exemplo). 

O cálculo é feito dividindo os quilômetros por 1.61, e o resultado é arredondado com a função **round**, que deixa o número com apenas duas casas decimais, facilitando a leitura. O programa mostra o resultado em milhas e encerra. 

```ruby
while True:
    try: 
        km = float(input('Quantos km você quer converter para milhas? '))
        resultado_milhas = round(km / 1.61, 2)
        print('Resultado:', resultado_milhas, 'milhas')
        break

    except ValueError:
        print('Digite apenas números que façam sentido para km!')
```


> **Exercício 1.2.3**

```3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?```

Escolhi integrar o que já tinha feito nos exercícios anteriores e criar um programa que faz as duas perguntas (tempo e distância) e ainda calcula o passo médio da corrida. Cuidei para que o programa trate os erros que podem acontecer quando o usuário digita algo errado, evitando que ele quebre. Também organizei os loops para que não fiquem infinitos, permitindo que o usuário escolha quando quer sair do programa.

Esse código se tornou um programa interativo. Ele usa *listas de respostas* possíveis para “sim” e “não” para facilitar a interpretação das respostas do usuário. 

O programa funciona em várias etapas dentro de laços **while True**, garantindo que o usuário insira dados válidos, e utiliza o método **strip().lower()** para tratar as respostas de forma flexível, ignorando espaços extras e diferenças entre maiúsculas e minúsculas. 

Também permite que o usuário decida se quer usar os dados anteriores para calcular o passo médio ou se prefere sair do programa. Mensagens são mostradas em cada etapa para orientar o usuário, e o programa só termina quando o usuário decide sair.

```ruby
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

        except Exception:
            print(f'\nErro tipo: {Exception} Digite apenas números!')

    print ('\nLegal, você correu muito!')

    while True:
        try: 
            km = float(input('\nAgora digite quantos km você percorreu na sua corrida: '))
            resultado_milhas = float(round(km / 1.61, 2))
            print('\nVocê correu:', resultado_milhas, 'milhas')
            break

        except Exception:
            print(f'\nErro tipo: {Exception} Digite apenas números!')
    
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
```

# Capítulo 2: Variáveis, expressões e instruções

**Glossário:**
```
Variável – nome usado para guardar um valor (como uma “caixinha”). Não pode começar com número, nem conter espaço, acento, ou símbolos especiais. Também não pode ter nomes que sejam palavras reservadas do Python (ex: if, while).

Atribuição – quando damos um valor a uma variável, usando o = (ex: x = 5).

Expressão – qualquer coisa que tenha um valor: pode ser um número, operação matemática, ou combinação (ex: 2 + 3, "oi" + " mundo").

Operador – símbolo que faz uma operação (ex: +, -, *, /).

Concatenação de strings – juntar textos com o operador + (ex: "bom" + "dia" vira "bomdia").

Repetição de strings – usar * com strings para repetir (ex: "la" * 3 vira "lalala").

Ordem dos parênteses – parênteses mudam a ordem dos cálculos, assim como na matemática (ex: (2 + 3) * 4 ≠ 2 + (3 * 4)).

Comentário (#) – texto ignorado pelo Python; usado para anotar ou explicar o código.

Sintaxe – regras da linguagem Python. Se você quebrar essas regras (como esquecer : ou escrever algo fora do lugar), aparece um erro de sintaxe.

Erro de tempo de execução (runtime error) – erro que acontece enquanto o programa está rodando. Exemplo: tentar dividir por zero.

Erro semântico (semantic error) – quando o programa roda sem erro, mas faz a coisa errada (a lógica está errada).

Exception (exceção) – tipo especial de erro que pode ser tratado para evitar que o programa quebre. Exemplo: tentar converter texto em número e falhar.
```

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

skskjdjd

```ruby
frete_fixo = 3
frete_adicional = 0.75

while True:
    try:
        preco_livro = float(input('Qual o preço do livro? R$'))
        desconto = float(input('Quantos % de desconto a livraria ganha nessa compra? (ex: 20 para 20%) '))
        quantidade_atacado = int(input('Quantas unidades serão pedidas? '))
        
        porcentagem = float(desconto)/100
        preco_com_desconto = (preco_livro * quantidade_atacado) * porcentagem
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

