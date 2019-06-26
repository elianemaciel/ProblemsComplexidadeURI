# -*- coding: utf-8 -*-
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)


NINF = -9999999
dp = []
num = 0
valor = []
comprimento = []

@lru_cache(maxsize=None, typed=False)
def solve(i, tamanho):
    global NINF, dp, num, valor, comprimento

    if i == num or tamanho == 0:
        return 0
   
    if tamanho < 0:
        return NINF
    
    if dp[i][tamanho] != -1:
        return dp[i][tamanho]
    if comprimento[i] > tamanho:
        dp[i][tamanho] = solve(i+1, tamanho)
        return dp[i][tamanho]
    
    dp[i][tamanho] = max(
        solve(i + 1, tamanho),
        valor[i] + solve(i, tamanho - comprimento[i])
    )
    return dp[i][tamanho]


def main():
    global NINF, dp, num, valor, comprimento
    
    result = []

    import sys
    sys.stdin = open('teste.txt')
    
    while True:
        try:
            line = input().split()
        except EOFError:
            break 
        num = int(line[0])
        tam = int(line[1])
        comprimento = []
        valor = []
        for i in range(num):
            lines = input().split()
            comprimento.insert(i, int(lines[0]))
            valor.insert(i, int(lines[1]))

        dp = [[-1 for i in range(2005)] for i in range(1005)]

        result.append(solve(0, tam))
    
    for i in result:
        print(i)

main()
