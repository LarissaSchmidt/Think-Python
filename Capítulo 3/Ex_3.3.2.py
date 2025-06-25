def desenha_grade_4x4():
    def linha_horizontal():
        print('+', '- ' * 9, '+', '- ' * 9, '+', '- ' * 9, '+', sep='')

    def linha_vertical():
        for _ in range(4):
            print('|', ' ' * 18, '|', ' ' * 18, '|', ' ' * 18, '|', sep='')

    def colunas(f):
        f()
        f()

    linha_horizontal()
    colunas(linha_vertical)
    linha_horizontal()
    colunas(linha_vertical)
    linha_horizontal()
    colunas(linha_vertical)
    linha_horizontal()

desenha_grade_4x4()