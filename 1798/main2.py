# -*- coding: utf-8 -*-


def main():

    result = []
    comprimento = []
    valor = []

    # import sys
    # sys.stdin = open('teste.txt')

    try:
        line = input().split()
    except EOFError:
        pass
    num = int(line[0])
    tam = int(line[1])

    for i in range(num):
        lines = input().split()
        comprimento.insert(i, int(lines[0]))
        valor.insert(i, int(lines[1]))
    result = [0 for i in range(2005)]

    for i in range(tam+1):
        result[i] = result[i-1]
        for j in range(num):
            if(comprimento[j] <= i and result[i] < result[i-comprimento[j]] + valor[j]):
                result[i] = result[i-comprimento[j]]+ valor[j]
    print(result[tam])

main()
