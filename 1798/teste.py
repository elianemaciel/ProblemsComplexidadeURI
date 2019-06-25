# -*- coding: utf-8 -*-

dp = []
num = 0
valor = []
comprimento = []

def solve(t, id):
    global dp, num, valor, comprimento
    if id >= num:
        return 0
    if t <= 0:
        return 0
    if dp[t][id] != -1:
        return dp[t][id]
    best = solve(t, id + 1)
    if t >= comprimento[id]:
        best = max(best, solve(t - comprimento[id], id) + valor[id])
    dp[t][id] = best
    return dp[t][id]

def main():
    global dp, num, valor, comprimento

    import sys
    sys.stdin = open('teste.txt')
    line = raw_input().split()
    num = int(line[0])
    tam = int(line[1])
    result = []

    for i in range(num):
        lines = raw_input().split()
        comprimento.insert(i, int(lines[0]))
        valor.insert(i, int(lines[0]))

    dp = [[-1 for i in range(2005)] for i in range(1005)]
    solved = solve(tam, 0)

    print solved


main()
