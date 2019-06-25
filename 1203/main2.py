# -*- coding: utf-8 -*-


def solve(vet, i, parc, pontes, regioes):
    if i >= regioes or (not vet[i]):
        return 0
    parc += vet[i]
    if parc == pontes:
        return 1
    if parc > pontes:
        return solve(vet, i+1, parc-vet[i], pontes, regioes)
    if solve(vet, i+1, parc, pontes, regioes):
        return 1
    return solve(vet, i+1, parc-vet[i], pontes, regioes)


def main ():
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
        vet = [0 for i in range(regioes)]
        for v in range(pontes):
            line = raw_input().split()
            line = list(map(int, line))
            vet[line[0]-1] += 1
            vet[line[1]-1] += 1
        vet.sort()
        results.append(solve(vet, 0, 0, pontes, regioes))
    for i in results:
        if i:
            print "S"
        else:
            print "N"

main()
