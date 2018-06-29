
# Info:
# [0000]Operação;[0000]Endereço_Resultado;[0000]Endereço_1; [0000]Endereço_2; [0]Tag = 17bits
# Instruções:
# 0001: Soma
# 0010: Sub
# 0100: Load
# 1000: Store

# Registradores:


InstrType = ''

# Abrir arquivo de Memória para leitura
# file = open('progMemory.txt', 'r')
# Abrir arquivo de Programa para leitura
# file = open('code.txt', 'r')





def decode(Instr):


    InstrType = Instr[:4]

    try:
        InstrType = int(InstrType,2)
    except:
        print(InstrType)
        print(type(InstrType))

    if InstrType == 1 :
        # Add

        print('SOMANDO...\n')

        fileA = open('0011.txt', 'r')
        fileB = open('0010.txt', 'r')

        for lineA in fileA:

            lineA = lineA.rstrip()
            InstrA = lineA

            try:
                A = int(InstrA)
            except:
                print(InstrA)
                print(type(InstrA))

        for lineB in fileB:

            lineB = lineB.rstrip()
            InstrB = lineB

            try:
                B = int(InstrB)
            except:
                print(InstrB)
                print(type(InstrB))



        C = A + B


        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))
        print('Result: {}'.format(C))

        fileMem = open('0000.txt','a')
        fileMem.write('{}'.format(C) + '\n')
        fileMem.close()




    elif InstrType == 2:
        # Sub
        print('SUBTRAINDO...\n')

        fileA = open('0011.txt', 'r')
        fileB = open('0010.txt', 'r')

        for lineA in fileA:

            lineA = lineA.rstrip()
            InstrA = lineA

            try:
                A = int(InstrA)
            except:
                print(InstrA)
                print(type(InstrA))

        for lineB in fileB:

            lineB = lineB.rstrip()
            InstrB = lineB

            try:
                B = int(InstrB)
            except:
                print(InstrB)
                print(type(InstrB))


        C = A - B


        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))
        print('Result: {}'.format(C))

        fileMem = open('0000.txt','a') #parâmetro 'a' é pra adicionar o conteúdo no final do arquivo
        fileMem.write('{} '.format(C) + '\n')
        fileMem.close()



    elif InstrType == 4:
        # Load:
        print('LOADING...\n')
        print('RegDest: {}'.format(Instr[4:8]))
        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))


    elif InstrType == 8:
        # Store:
        print('STORING...\n')
        print('RegDest: {}'.format(Instr[4:8]))
        print('RegSourceA: {}'.format(Instr[8:12]))
        print('RegSourceB: {}'.format(Instr[12:16]))


    print('\n\nDecoded!')






def execute(Instr):


    print('\n\nCommand: {}'.format(Instr[:4]),'\n')

    decode(Instr)
    print('-------------------------------------')


PC = 0;
cache = [None, None, None, None, None, None]
# Execução com for rodando todas as linhas do programa e executando direto

def run(PC, cache):

    file = open('comandos.txt', 'r')


    for line in file:
        line = line.rstrip()
        Instr = line


        if cache[PC] == Instr and Instr[16] == '1':
            print("Cache HIT")
            cacheInstr = cache[PC]

            try:
                execute(cacheInstr)

            except:
                print(cacheInstr)
                print(type(cacheInstr))


        else:
            print("Cache MISS")
            cache[PC] = Instr
            line = ' '
            try:
                execute(Instr)

            except:
                print(Instr)
                print(type(Instr))

        PC += 1

    file.close()

run(PC, cache)
run(PC, cache)
