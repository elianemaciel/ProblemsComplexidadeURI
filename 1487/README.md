
# 1487 Six Flags


O Six Flags Fiesta Texas é um dos maiores parques de diversão do mundo, e fica em San Antonio. Sabendo que as finais do ACM-ICPC de 2006 serão naquela cidade, três colegas começaram a planejar em quais dos famosos brinquedos eles iriam, caso seu time se classificasse para as finais mundiais.

Para isso, estabeleceram notas para cada uma das atrações de acordo com o quanto eles gostariam de brincar lá. Por exemplo, a montanha russa "Superman Krypton Coaster" (que tem 800m de giros, loops e quedas com o carrinho indo a mais de 100km/h) recebeu a maior pontuação possível entre os colegas.

O problema é que é impossível visitar todas as atrações em um mesmo dia. Assim, os colegas pesquisaram, para cada uma delas, quanto tempo durava o brinquedo (e quanto tempo de fila teriam de enfrentar até chegar a ele...). Sua tarefa neste problema é encontrar, dado o tempo disponível pelos colegas no Six Flags, uma coleção (pode haver repetições) de atrações que dá a maior pontuação dentro deste período.

## Entrada

Seu programa deve estar preparado para processar diversas instâncias. Na primeira linha são dados dois inteiros 0 ≤ N ≤ 100 e 0 ≤ T ≤ 600, em que N é o número de atrações nas quais os colegas gostariam de brincar, e T é o tempo (em minutos) que eles terão disponível para isso. Nas próximas N linhas, são dados dois inteiros 0 ≤ D ≤ 600 e 0 ≤ P ≤ 100 (em cada linha). O primeiro deles, D, representa a duração do brinquedo (incluído aí o tempo de fila e uma estimativa do tempo de traslado entre os brinquedos). O segundo, P, representa a pontuaçãao atribuída ao brinquedo pelos colegas. Um valor N = 0 indica o final das instâncias e não deverá ser processado.

## Saída

Para cada instância solucionada, você deverá imprimir um identificador Instancia H em que H é um número inteiro, sequencial e crescente a partir de 1. Na linha seguinte, deve ser impressa a pontuação total conseguida com a coleção determinada por seu programa. Com relação a quais são as atrações da coleção determinada, os colegas decidiram que iriam perguntar para você pessoalmente no futuro, já que eles não querem que outras pessoas saibam e venham a utilizá-la. Uma linha em branco deve ser impressa após cada caso de teste.
