# -*- coding: utf-8 -*-

POSSIVEL = 0
REGIOES =0
PONTES =0
GRAU = []
DP = []

def solve(regiao, restam):
    global DP, GRAU, POSSIVEL, REGIOES, PONTES

    if POSSIVEL:
        return 1
    elif restam < 0 or regiao > REGIOES:
        return 0
    elif restam == 0:
        POSSIVEL = 1
        DP[regiao][restam] = 1
        return DP[regiao][restam]
    elif DP[regiao][restam] != -1:
        return DP[regiao][restam]
    solved = solve(regiao+1,restam)
    if solved:
        DP[regiao][restam] = solved
    else:
        DP[regiao][restam] = solve(regiao+1,restam - GRAU[regiao])

    return DP[regiao][restam]

def main():
    global POSSIVEL, GRAU, DP, REGIOES, PONTES
    results = []

    try:
        import sys
        sys.stdin = open('teste.txt')

        while True:
            try:
                lines = raw_input().split()
            except EOFError:

                break
            REGIOES = int(lines[0])
            PONTES = int(lines[1])
            POSSIVEL = 0
            DP = [[] for i in range(REGIOES+1)]
            GRAU = [0 for i in range(REGIOES+1)]

            for i in DP:
                for j in range(PONTES+1):
                    i.append(-1)
            for v in range(PONTES):
                line = raw_input().split()
                cid_a = int(line[0])
                cid_b = int(line[1])
                GRAU[cid_a] += 1
                GRAU[cid_b] += 1
            solved = solve(0, PONTES)
            if solved:
                results.append('s')
            else:
                results.append('n')
        for i in results:
            print i
        print
    except Exception as e:
        print e
        pass

main()
