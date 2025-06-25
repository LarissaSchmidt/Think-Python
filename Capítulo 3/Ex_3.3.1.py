def grade():
    def linha(): 
        print ('+', '- - - - ', '+', '- - - - ', '+')
    def coluna():
        print ('|', ' ' * 8, '|', ' ' * 8, '|', ' ' * 8)
    def mais(f):
        f()
        f()
        f()
        f()
    linha()
    mais(coluna)
    linha()
    mais(coluna)
    linha()

grade()