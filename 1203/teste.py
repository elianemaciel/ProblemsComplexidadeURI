# -*- coding: utf-8 -*-
import ipdb

MAXR = 101
MAXK = 10010
possivel = 0
r =0
k =0
grau = []
dp = []

def solve(regiao, restam):
    global dp, grau, possivel
    if possivel:
        return 1
    elif restam < 0 or regiao > r:
        return 0
    elif restam == 0:
        possivel = 1
        dp[regiao-1][restam-1] = 1
        return dp[regiao][restam]
    elif dp[regiao-1][restam-1] != -1:
        print(regiao, restam)
        return dp[regiao][restam]
    print("DD")
    dp[regiao][restam] = solve(regiao+1,restam) or solve(regiao+1,restam - grau[regiao])
    return dp[regiao][restam]

def main():
    global possivel
    pontes = []
    global grau
    global dp
    import sys
    sys.stdin = open('teste.txt')
    
    while True:
        try:
            n = input()
        except EOFError:

            break
        a = n.split(' ')
        k = int(a[1])
        r = int(a[0])
        possivel = 0
        grau = []
        dp = []
        for i in range(r):
            grau.insert(i, 0)
            dp.append([])
            for j in range(k):
                dp[i].append(-1)
        for v in range(k):
            line = input()
            elements = line.split(' ')
            u = int(elements[0]) - 1 
            v = int(elements[1]) - 1 
            print(u, v)
            grau[u] += 1
            grau[v] += 1
        
        import IPython
        IPython.embed()
        if solve(1, k):
            print('S')
        else:
            print('N')
        # printf("%c\n",solve(1,k) ? 'S' : 'N');



main()