# -*- coding: utf-8 -*-

MAXN = 112
MAXW  = 612

NUM = 0
TEMPO = 0
DURACAO = []
PONTOS = []
MAXI = []


def solve(pos, tem):
    global NUM, MAXI, DURACAO, PONTOS
    if pos == NUM or tem == 0:
        return 0
    if MAXI[pos][tem] != -1:
        return MAXI[pos][tem]
    if DURACAO[pos] > tem:
        MAXI[pos][tem] = solve(pos+1, tem)
        return MAXI[pos][tem]
    MAXI[pos][tem] = max(
        solve(pos+1, tem),
        max(
            solve(pos+1, tem - DURACAO[pos]) + PONTOS[pos],
            solve(pos, tem - DURACAO[pos]) + PONTOS[pos]
        )
    )
    return MAXI[pos][tem]


def main():
    import time
    count = 0
    global DURACAO,  PONTOS, TEMPO, NUM, MAXI
    inicio = time.time()
    import sys
    sys.stdin = open('teste.txt')
    result = []
    while True:
        line = raw_input().split()
        NUM = int(line[0])
        TEMPO = int(line[1])
        MAXI = []
        for i in range(112):
            MAXI.append([])
            for j in range(612):
                MAXI[i].append(-1)
        if NUM == 0 and TEMPO == 0:
            break
        for i in range(NUM):
            lines = raw_input().split(' ')
            DURACAO.insert(i, int(lines[0]))
            PONTOS.insert(i, int(lines[1]))
        solved = solve(0, TEMPO)
        result.append(solved)
    for inst in enumerate(result):
        print("Instancia %d\n%d\n" % (inst[0]+1, inst[1]))

    fim = time.time()
    print(fim - inicio)

main()
