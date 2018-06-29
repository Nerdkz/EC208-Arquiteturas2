# Info:
# [0000]Operação;[0000]Endereço_Resultado;[0000]Endereço_1; [0000]Endereço_2
# Instruções:
# 0001: Soma
# 0010: Sub
# 0100: Load
# 1000: Store

def parse(value):

    op = (value & 0xf000) >> 12
    res = (value & 0x0f00) >> 8
    end1 = (value & 0x00f0) >> 4
    end2 = (value & 0x000f) >> 0

    return op, res, end1, end2

def operation(value):
    op, res, end1, end2 = parse(value)
    if op == 0x1:
        











value = int(input('Entre com o número: '), 2)

op, res, end1, end2 = parse(value)
print('{} {} {} {}'.format(op, res, end1, end2))

#resultado = bin(num1 + num2)[2:]

#resultado = str(resultado).replace(resultado[2:], '')

#print('Resultado em binário = {}'.format(resultado))
