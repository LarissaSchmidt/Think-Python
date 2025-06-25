# Capítulo 3: Funções

> **Exercício 3.1**

Iniciamos definindo a função ```right_justify```, que receberá como parâmetro uma *string* chamada ```monty```. Dentro dessa função, utilizamos um bloco ```try``` para garantir que, caso algum erro ocorra, o programa não seja interrompido de forma inesperada, permitindo tratá-lo de maneira adequada.

```ruby
def right_justify (monty):
    try:
```
Logo na primeira verificação, usamos ```isinstance``` para garantir que o valor passado seja realmente uma *string*. Caso não seja, um erro do tipo ```TypeError``` é lançado manualmente com a mensagem "*Digite uma frase.*".

```ruby
def right_justify (monty):
    try:
        if not isinstance(monty, str):
            raise TypeError('Digite uma frase.')
```

Em seguida, usamos a função ```len(monty)``` para calcular o *número de caracteres da string* digitada, armazenando esse valor na variável ```comprimento```.

```ruby
    comprimento = len(monty)
```

Para tornar a visualização do alinhamento mais clara no terminal, imprimimos uma linha horizontal com ```print('\n' + '=' * 80)```, seguida do título "*Justificador de Texto até a coluna 70 📏*", e logo abaixo uma linha com 70 espaços seguidos de um caractere de barra vertical (|), que serve como marcador visual da posição onde a *string* deve terminar. Abaixo dele, uma seta para baixo (*↓*) reforça esse ponto.

```ruby
        print('\n' + '=' * 80)
        print('Justificador de Texto até a coluna 70 📏\n')
        print(' ' * 70 + '|\n')
        print(' ' * 70 + '↓\n')
```

Verificamos então com um bloco ```if```, se a frase digitada é maior que 70 caracteres. Se for, exibimos uma mensagem informando que a frase é muito longa e mostramos quantos caracteres ela possui.

```ruby
    if comprimento > 70:
            print(f'⚠️ Sua frase tem {comprimento} caracteres.')
            print('Você digitou uma frase muito longa!')
 ```

Caso a frase tenha até 70 caracteres, calculamos a quantidade de espaços que devem ser inseridos antes da frase para que ela termine exatamente na coluna 70. Essa quantidade é obtida subtraindo o comprimento da frase de 70 e armazenando esse valor na variável ```espacos```. Em seguida, multiplicamos um caractere de espaço por esse valor para gerar a *indentação* e *concatenamos* com a frase. O resultado é armazenado na variável ```resultado``` e exibido com a mensagem “*🡆 Resultado justificado:*”.

```ruby
     else:
            espacos = 70 - comprimento
            resultado = ' ' * espacos + monty
            print(f'🡆 Resultado justificado:\n {resultado}')
```

Ao final do bloco ```try```, imprimimos novamente uma linha horizontal para delimitar visualmente o fim da execução da função.

```ruby
    print('\n' + '=' * 80)
```

Se o tipo de dado passado à função não for uma *string*, o ```except TypeError``` captura esse erro e exibe a mensagem correspondente. Já o ```except Exception``` funciona como um tratamento genérico para qualquer outro erro inesperado, exibindo sua mensagem.

```ruby
except TypeError as te:
        print(f'Erro de tipo {te}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado {e}')
```

A função ```main_programa``` é responsável por interagir com o usuário. Nela, pedimos ao usuário que digite uma palavra ou frase por meio da função ```input```. O valor digitado é armazenado na variável ```entrada```.

```ruby
def main_programa():
    try:
        entrada = input('Digite uma palavra ou frase para justificar até a coluna 70: ')

        right_justify(entrada)

    except Exception as e:
        print(f'Ocorreu um erro inesperado {e}')

main_programa()
```

Em seguida, chamamos a função ```right_justify``` e passamos a entrada como argumento. Por fim, um bloco ```try/except``` envolve essa interação para lidar com eventuais erros na entrada do usuário, exibindo uma mensagem apropriada caso algo dê errado.

No total temos o código:

```ruby
def right_justify (monty):
    try:
        if not isinstance(monty, str):
            raise TypeError('Digite uma frase.')
        
        comprimento = len(monty)

        print('\n' + '=' * 80)
        print('Justificador de Texto até a coluna 70 📏\n')
        print(' ' * 70 + '|\n')


        if comprimento > 70:
            print(f'⚠️ Sua frase tem {comprimento} caracteres.')
            print('Você digitou uma frase muito longa!')
        else:
            espacos = 70 - comprimento
            resultado = ' ' * espacos + monty
            print(f'🡆 Resultado justificado:\n {resultado}')

        print('\n' + '=' * 80)

    except TypeError as te:
        print(f'Erro de tipo {te}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado {e}')
        
def main_programa():
    try:
        entrada = input('Digite uma palavra ou frase para justificar até a coluna 70: ')

        right_justify(entrada)

    except Exception as e:
        print(f'Ocorreu um erro inesperado {e}')

main_programa()
```

A linha ```main_programa()``` na última linha do código executa a função principal do programa, iniciando sua execução. Sem ela, o Python apenas carregaria as definições das funções, mas nada seria rodado automaticamente.

Caso digitemos a frase "*Este é o resultado esperado para uma frase do usuário*", é isso que teremos como resultado no terminal:

*Resultado* 

``` 
================================================================================
Justificador de Texto até a coluna 70 📏

                                                                      |

                                                                      ↓

🡆 Resultado justificado:
                  Este é o resultado esperado para uma frase do usuário

================================================================================
```

> **Exercício 3.2**

Definimos ```def do_twice(f)``` e assim criamos uma função que recebe um objeto de função ```(f)``` e o chama duas vezes (com ```f()``` em duas linhas).

```ruby
#3.2.1
def do_twice(f):
    f()
    f()
```

Em seguida, definimos ```def print_spam()```, que simplesmente imprime a palavra *spam*. 

```ruby
def print_spam():
    print('spam')

do_twice(print_spam)
```

Por fim, testamos o exemplo original chamando ```do_twice(print_spam)```, o que faz *spam* aparecer duas vezes na tela.

*Resultado*
```
spam
spam
```

Alteramos ```do_twice``` para ```do_twice_arg(f, value)```. Essa função agora recebe dois parâmetros:

```f```: o objeto de função a ser chamado.

```value```: o valor que queremos passar para f.

```ruby
#3.2.2 
def do_twice_arg(f, value):
    f(value)
    f(value)
```

Chamamos ```f(value)``` em duas linhas, garantindo que ```f``` receba ```value``` a cada execução.

Copiamos a definição de ```print_twice(x)```. Essa função imprime o argumento *x* duas vezes. Ela será usada para demonstrar como passar valores através de ```do_twice_arg```.

```ruby
#3.2.3 
def print_twice(x):
    print(x)
    print(x)
```

Chamamos ```do_twice_arg(print_twice, 'mensagem')```. Aqui passamos ```print_twice``` como função e a string *mensagem* como valor.

```ruby
#3.2.4 
do_twice_arg(print_twice, 'mensagem')
```

*Resultado*

```
mensagem
mensagem
mensagem
mensagem
```

Definimos então ```do_four(f, value)```, para criar uma função que chame ```f(value)``` quatro vezes, reutilizamos ```do_twice_arg``` duas vezes dentro de ```do_four```. Assim, mantemos apenas duas linhas no corpo de ```do_four```, mas geramos quatro chamadas.

```ruby
#3.2.5 
def do_four(f, value):
    do_twice_arg(f, value)
    do_twice_arg(f, value)

do_four(print_twice, 'spam')
```

Testamos ```do_four(print_twice, 'spam')```. Chamando essa função, obtemos oito linhas de *spam* (duas impressões de ```print_twice``` vezes quatro chamadas totais).

*Resultado*

```
spam
spam
spam
spam
spam
spam
spam
spam
```

No total temos o código:

```ruby
#3.2.1 
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

#3.2.2 
def do_twice_arg(f, value):
    f(value)
    f(value)

#3.2.3 
def print_twice(x):
    print(x)
    print(x)

#3.2.4 
do_twice_arg(print_twice, 'mensagem')

#3.2.5 
def do_four(f, value):
    do_twice_arg(f, value)
    do_twice_arg(f, value)

do_four(print_twice, 'spam')
```

Aqui, observamos como funções podem ser tratadas como objetos em Python, sendo passadas como argumentos e chamadas dentro de outras funções. Esses exemplos evidenciam a versatilidade da linguagem e mostram como estruturar o código de forma modular e reutilizável ao utilizar funções como parâmetros.

> **Exercício 3.3**

 
