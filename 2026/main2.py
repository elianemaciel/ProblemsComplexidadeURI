# -*- coding: utf-8 -*-

PACOTES = 0
CAPACIDADE = 0
VET = []
ENFEITES = []
PESO_PAC = []

def solve(pos, capacidade):
    global PACOTES, VET, PESO_PAC, ENFEITES, CAPACIDADE

    if pos == PACOTES or capacidade == 0:
        return 0
    if VET[pos][capacidade] != -1:
        return VET[pos][capacidade]
    if PESO_PAC[pos] > capacidade:
        VET[pos][capacidade] = solve(pos+1, capacidade)
        return VET[pos][capacidade]
    VET[pos][capacidade] = max(
        solve(pos+1, capacidade),
        ENFEITES[pos] + solve(pos+1, capacidade - PESO_PAC[pos])
    )
    return VET[pos][capacidade]


def main():
    global VET, PACOTES, ENFEITES, PESO_PAC

    VET = [[-1 for i in range(1000)] for i in range(1000)]

    # import sys
    # sys.stdin = open('teste.txt')
    galhos = int(input())
    result = []

    for i in range(galhos):
        PACOTES = int(raw_input())
        CAPACIDADE = int(raw_input())
        ENFEITES = []
        PESO_PAC = []
        VET = [[-1 for i in range(1000)] for i in range(1000)]
        for j in range(PACOTES):
            line = raw_input().split()
            ENFEITES.insert(j, int(line[0]))
            PESO_PAC.insert(j, int(line[1]))
        solved = solve(0, CAPACIDADE)
        result.append(solved)

    for i in enumerate(result):
        print("Galho %d:" % (i[0]+1))
        print("Numero total de enfeites: %d\n" % i[1])
    return

main()
