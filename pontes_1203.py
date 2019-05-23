# -*- coding: utf-8 -*-

'''
1203 - Pontes de São Petersburgo

Todos conhecem o famoso problema das pontes de Königsberg, cidade da Prússia que ficou famosa pelo problema resolvido por
Euler ainda no século XVIII. Poucos conhecem, entretanto, o problema das pontes de São Petersburgo.
A cidade de São Petersburgo localiza-se às margens do Rio Neva, e é cruzada por dezenas de pontes que
ligavam as margens do rio às centenas de pequenas ilhas que o rio possui. Os moradores da cidade, conhecedores
do famoso problema das pontes de Königsberg, criaram seu próprio problema. Os moradores sabem que existem K
pontes na cidade, que são R regiões distintas na cidade e que cada ponte liga exatamente 2 regiões distintas da cidade.
Os moradores querem saber se, para a cidade deles, é possível escolher algumas destas regiões tais que o número de pontes
que incide em todas elas é igual a K. Note que, se duas destas regiões escolhidas tiverem uma ponte entre elas, esta ponte
será contada duas vezes.
Entrada

A entrada é composta por diversas instâncias e termina com final de arquivo (EOF).
A primeira linha de cada caso de teste contém dois números, R (2 ≤ R ≤ 100) e K (1 ≤ K ≤ R * (R-1) / 2),
o número de regiões e pontes da cidade, respectivamente. Por efeito de simplificação, as regiões são enumeradas de 1 até R, inclusive. A seguir temos K linhas, cada uma delas contendo dois números A e B, informando que existe uma ponte ligando as regiões A e B da cidade.
Saída

Para cada caso de teste imprima uma linha apenas com "S" (aspas apenas para evidenciar), se é possível
escolhermos as regiões da maneira descrita anteriormente, ou "N" (idem), se não for possível.

'''
