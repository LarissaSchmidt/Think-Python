# Think Python - How To Like a Computer Scientist
<img src="https://howtolearnmachinelearning.com/wp-content/uploads/2020/11/Think_Python.png" width="400">

# Glossário

> **Capítulo 1:**

**int**: número inteiro (ex: 1, 42, -7)

**float**: número decimal ou quebrado (ex: 3.14, -0.5)

**str**: string, sequência de caracteres ou texto (ex: 'olá', 'python')

**print**: função que exibe algo na tela

**input**: função que recebe uma entrada do usuário

**bug**: erro ou falha no código

**debugging**: processo de encontrar e corrigir bugs

**operator**: símbolo que realiza uma operação (ex: +, -, *, /)

**expression**: combinação de valores e operadores que Python pode avaliar (ex: 2 + 3)

**statement**: instrução completa que o Python executa (ex: print("oi"))

**variable**: nome que armazena um valor (ex: x = 5)

**assignment**: ação de atribuir um valor a uma variável (ex: x = 10)

**value**: dado armazenado ou manipulado pelo programa (ex: 42, "texto")

**type**: tipo de dado (ex: int, float, str)

**syntax**: conjunto de regras para escrever o código corretamente

**comment**: texto no código ignorado pelo Python, usado para explicações (# isso é um comentário)

**function**: bloco de código reutilizável que realiza uma tarefa (ex: print())

**parameter**: valor passado para uma função

**return**: valor que uma função devolve após executar

**prompt**: mensagem exibida para o usuário durante a entrada de dados (ex: input('Digite seu nome: '))

**^**: operador bitwise XOR (exclusive or) que compara bits (não muito usado no começo, mas aparece)

> **Capítulo 2:**

**Variável**: nome usado para guardar um valor (como uma “caixinha”). Não pode começar com número, nem conter espaço, acento, ou símbolos especiais. Também não pode ter nomes que sejam palavras reservadas do Python (ex: if, while).

**Atribuição**: quando damos um valor a uma variável, usando o = (ex: x = 5).

**Expressão**: qualquer coisa que tenha um valor: pode ser um número, operação matemática, ou combinação (ex: 2 + 3, "oi" + " mundo").

**Operador**: símbolo que faz uma operação (ex: +, -, *, /).

**Concatenação de strings**: juntar textos com o operador + (ex: "bom" + "dia" vira "bomdia").

**Repetição de strings**: usar * com strings para repetir (ex: "la" * 3 vira "lalala").

**Ordem dos parênteses**: parênteses mudam a ordem dos cálculos, assim como na matemática (ex: (2 + 3) * 4 ≠ 2 + (3 * 4)).

**Comentário (#)**: texto ignorado pelo Python; usado para anotar ou explicar o código.

**Sintaxe**: regras da linguagem Python. Se você quebrar essas regras (como esquecer : ou escrever algo fora do lugar), aparece um erro de sintaxe.

**Erro de tempo de execução (runtime error)**: erro que acontece enquanto o programa está rodando. Exemplo: tentar dividir por zero.

**Erro semântico (semantic error)**: quando o programa roda sem erro, mas faz a coisa errada (a lógica está errada).

**Exception (exceção)**: tipo especial de erro que pode ser tratado para evitar que o programa quebre. Exemplo: tentar converter texto em número e falhar.

> **Capítulo 3:**

**import**: Comando usado para carregar módulos externos no código.

**módulo**: Arquivo com código Python reutilizável (funções, variáveis, classes).

**notação de ponto**: Forma de acessar elementos de um módulo usando ponto (modulo.funcao).

**def**: Palavra-chave usada para definir uma função.

**argumentos**: Valores passados para uma função quando ela é chamada.

**function**: Bloco de código reutilizável que executa uma tarefa específica.

**fluxo de execução**: Ordem em que as instruções do programa são executadas.

**diagrama de pilha**: Representação visual dos frames (chamadas de função) durante a execução.

**frame**: Registro na pilha contendo informações de uma chamada de função (como variáveis locais).

**traceback**: Mensagem de erro que mostra a sequência de chamadas que levou a uma exceção.

> **Capítulo 4:**

**turtle**: Módulo gráfico do Python que permite controlar uma "tartaruga" que desenha na tela conforme se move.

**pu**/**pd**: Métodos do turtle para levantar (pu, "pen up") ou abaixar (pd, "pen down") a caneta, controlando se o movimento deixa rastro.

**fd**: Método que move a tartaruga para frente uma certa distância (em pixels).

**bk**: Método que move a tartaruga para trás uma certa distância (em pixels).

**lt**: Método que faz a tartaruga virar para a esquerda, em um ângulo especificado (em graus).

**rt**: Método que faz a tartaruga virar para a direita, em um ângulo especificado (em graus).

**for**: Estrutura de repetição usada para executar um bloco de código várias vezes, definida com ```for variável in range(n):```.

