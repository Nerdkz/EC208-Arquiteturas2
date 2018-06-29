
cache = [None, None, None, None, None,None,None, None]
PC = 0


def lerArquivo(PC, cache):

    file = open('comandos.txt', 'r')

    for line in file:

        line = line.rstrip()
        if cache[PC] == line:
            print("HIT")
        else:
            print("MISS")
            cache[PC] = line
            print(cache[PC])


    file.close()

lerArquivo(PC, cache)
