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