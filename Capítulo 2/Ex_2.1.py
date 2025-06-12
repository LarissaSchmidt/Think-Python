#42 = n da erro, número não guarda informação, não pode ser uma variável que recebe info
n = 42
print(n)

#Podemos atribuir um mesmo valor para variáveis de nome diferentes
x = y = 1
print(x)
print(y)
print(x+y)

#Apesar de ser possível utilizar o ; para separar variáveis, idealmente utiliza-se uma nova linha para cada informação adicionada. O ; só é usado se você quiser escrever duas instruções na mesma linha.
x = 5; y = 10
print(x+y)

#Já o ponto não deve ser utilizado, pois ele é utilizado em Python para acessar partes de algo, como deixar todas as letras de um input em caixa alta

nome = input('Qual o seu nome? ')
nome_maiusculo = nome.upper()
print(f'Olá {nome_maiusculo}!')

#Para multiplicar algo você precisa utilizar o operador *, sem ele o programa identificara xy como variável
print(x*y)