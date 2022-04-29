import csv

def codificar(entrada):
    if (entrada == '0'):
        return '1'
    elif (entrada == '1'):
        return '11'
    elif (entrada == 'B'):
        return '111'

def decodificar(entrada):
    if (entrada == '1'):
        return '0'
    elif (entrada == '11'):
        return '1'
    elif (entrada == '111'):
        return 'B'

def MTU():
    with open('exemplo2.csv', 'r') as file:
        reader = csv.reader(file)
        entrada = []
        for row in reader:
            entrada = row

    binarios = entrada[0].split(';')

    fita1 = '00010101010110010110101101100101110110111011001101011010110011011011011011001101110111011101001110101110110100111011011110101001110111011111101110110011110101111010100111101101111011010011110111011111011101001111101010110110011111011011111010100111110111010110110011111101101111110111011001111110111011111110111011000'
    fita2 = '1' # estado q0 codificado
    fita3 = 'B' + binarios[0] + 'B' + binarios[1] + 'BB' # entrada w

    transicoes = fita1.split('000')
    transicoes = transicoes[1].split('00')

    cabeca_leitura = 1
    rodando = True
    while(rodando):
        estado = fita2
        simbolo = fita3[cabeca_leitura]
        
        transicao_encontrada = False
        for transicao in transicoes:
            componentes = transicao.split('0')
            if (componentes[0] == estado and componentes[1] == codificar(simbolo)): #qi == estado && x == simbolo
                transicao_encontrada = transicao
                break

        if (transicao_encontrada):
            componentes = transicao.split('0')

            fita2 = componentes[2] # qj
            fita3 = fita3[:cabeca_leitura] + decodificar(componentes[3]) + fita3[cabeca_leitura+1:] #y

            if (componentes[4] == '1'): # L
                cabeca_leitura = cabeca_leitura - 1
            elif (componentes[4] == '11'): # R
                cabeca_leitura = cabeca_leitura + 1

        else:
            rodando = False

    resultado = fita3.replace('B', '')
    print(resultado)

MTU()
