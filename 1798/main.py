# -*- coding: utf-8 -*-

NINF = -9999999
dp = [[-1 for i in range(2005)] for i in range(1005)]
num = 0
valor = []
comprimento = []

def solve(i, tamanho):
    global NINF, dp, num, valor, comprimento
    print i, tamanho
    if i == num:
        return 0
    if tamanho == 0:
        return 0
    if tamanho <= 0:
        return NINF

    ans = dp[i][tamanho]
    if ans == -1:
        ans = max(solve(i + 1, tamanho), valor[i] + solve(i, tamanho - comprimento[i]))
	return ans

      if (id >= a.size()) return 0;
  if (t <= 0) return 0;
  if (dp[t][id] != -1) return dp[t][id];
  int best = go(a, t, id + 1);
  if (t >= a[id].len)
    best = max(best, go(a, t - a[id].len, id) + a[id].cost);
return dp[t][id] = best;


def main():
    global NINF, dp, num, valor, comprimento

    # import ipdb; ipdb.set_trace()
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


    solved = solve(0, tam)
    print solved

main()
