# -*- coding: utf-8 -*-

def solve(regiao, restam, dp, grau, possivel, regioes, pontes):

    if possivel:
        return 1
    if restam < 0 or regiao > regioes:
        return 0
    if restam == 0:
        possivel = 1
        dp[regiao][restam] = 1
        return dp[regiao][restam]
    if restam > pontes:
        return solve(regiao+1, restam-grau[regiao], dp, grau, possivel, regioes, pontes);
    if dp[regiao][restam] != -1:
        return dp[regiao][restam]
    if  solve(regiao+1, restam, dp, grau, possivel, regioes, pontes):
        return 1

    return solve(regiao+1, restam - grau[regiao], dp, grau, possivel, regioes, pontes)


def main():
    possivel = 0
    regioes = 0
    pontes = 0
    grau = []
    dp = []
    results = []

    import sys
    sys.stdin = open('teste.txt')

    while True:
        try:
            lines = raw_input().split()
        except EOFError:

            break
        regioes = int(lines[0])
        pontes = int(lines[1])
        possivel = 0
        dp = [[-1 for j in range(pontes+1)] for i in range(regioes+1)]
        grau = [0 for i in range(regioes+1)]
        for v in range(pontes):
            line = raw_input().split()
            cid_a = int(line[0])
            cid_b = int(line[1])
            grau[cid_a] += 1
            grau[cid_b] += 1
        results.append(solve(0, pontes, dp, grau, possivel, regioes, pontes))

    for i in results:
        if i:
            print 'S'
        else:
            print 'N'
    print ""

if __name__ == "__main__":
    main()
