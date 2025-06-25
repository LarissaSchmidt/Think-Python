def repetir_duas_vezes(acao):
    acao()
    acao()

def repetir_quatro_vezes(acao):
    repetir_duas_vezes(acao)
    repetir_duas_vezes(acao)

def desenha_grade_4x4():
    def desenha_linha_horizontal():
        print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', sep='')

    def desenha_linha_vertical():
        print('|', ' ' * 8, '|', ' ' * 8, '|', ' ' * 8, '|', ' ' * 8, '|', sep='')

    def bloco_grade():
        desenha_linha_horizontal()
        repetir_quatro_vezes(desenha_linha_vertical)

    repetir_quatro_vezes(bloco_grade)
    desenha_linha_horizontal()

desenha_grade_4x4()