# -*- coding: utf-8 -*-


MAXP = 112
MAXW = 1123

PACOTES = 0
CAPACIDADE = 0
VET = []
ENFEITES = []
PESO_PAC = []

def solve(pos, capacidade):
    global PACOTES, VET, PESO_PAC
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
    import sys
    sys.stdin = open('teste.txt')
    galhos = int(input())
    global VET, PACOTES, ENFEITES, PESO_PAC
  
    for i in range(112):
        VET.append([])
        for j in range(612):
            VET[i].append(-1)
    for i in range(galhos):
        PACOTES = int(input())
        CAPACIDADE = int(input())
        for j in range(PACOTES):
            line = input().split(' ')
            ENFEITES.insert(j, int(line[0]))
            PESO_PAC.insert(j, int(line[1]))
        print("Galho %d:" % (i+1))
        print("Numero total de enfeites: %d\n" % solve(0, CAPACIDADE))
    return

main()