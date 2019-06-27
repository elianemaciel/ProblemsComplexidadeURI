# -*- coding: utf-8 -*-

ci = [] # tamanho de cada cano
vi = [] # valor de cada cano

m = []

def main():

    m = [0 for i in range(2000)]
    # scanf("%d",&NC);
    # scanf("%d",&TC);

    import sys
    sys.stdin = open('teste.txt')

    lines = input().split()

    NC = int(lines[0])
    TC = int(lines[1])

    for i in range(NC):
        line = input().split()
        ci.insert(i, int(line[0]))
        vi.insert(i, int(line[1]))
        # scanf("%d%d",&ci[i],&vi[i]);
    m.append(0)
    for w in range(TC+1):
        m[w] = m[w-1];
        for j in range(NC):
            if(ci[j] <= w):
                if(m[w] < m[w-ci[j]] + vi[j]):
                    m[w] = m[w-ci[j]]+ vi[j]
    print(m[TC]);
    return 0

main()
