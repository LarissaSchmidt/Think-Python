# Capítulo 3: Funções

> **Exercício 3.1**

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

1
