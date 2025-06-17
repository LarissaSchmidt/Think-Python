# 1. Exemplo original: função que chama outra função duas vezes
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

# Teste do exemplo original
do_twice(print_spam)


# 2. Versão alterada de do_twice: recebe uma função e um valor, e passa esse valor
#    como argumento em cada chamada
def do_twice_arg(f, value):
    f(value)
    f(value)


# 3. Definição de print_twice (imprime o argumento duas vezes)
def print_twice(x):
    print(x)
    print(x)


# 4. Usando do_twice_arg para chamar print_twice duas vezes, passando 'spam'
do_twice_arg(print_twice, 'spam')


# 5. Definição de do_four: chama quatro vezes a função passada, com o valor informado.
#    Aqui usamos do_twice_arg dentro de do_four para manter o corpo com apenas duas linhas.
def do_four(f, value):
    do_twice_arg(f, value)
    do_twice_arg(f, value)


# Teste de do_four com print_twice e 'spam'
do_four(print_twice, 'spam')