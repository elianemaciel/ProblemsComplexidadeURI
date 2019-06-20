#include <stdio.h>
#include <string.h>

// Retorna o maior
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define TRUE 1
#define max_nro_pedidos 20
#define max_nro_max_pizzas 30

int calcula(int nro_max_pizzas, int nro_pedidos, int ans[max_nro_pedidos+1][max_nro_max_pizzas+1], int quantidade_pizzas_pedido[max_nro_pedidos+1], int tempo_entrega[max_nro_pedidos+1]){
	
	int i,j;
	
	for(i=1 ; i<=nro_max_pizzas ; i++){
		for(j=0 ; j<nro_pedidos ; j++){
			if(j>0){				
				ans[j][i] = ans[j-1][i];
				if(quantidade_pizzas_pedido[j] <= i){
					ans[j][i] = MAX(ans[j][i], ans[j-1][i-quantidade_pizzas_pedido[j]] + tempo_entrega[j]);
				}
			} else{
				ans[j][i] = 0;
				if(quantidade_pizzas_pedido[j] <= i){
					ans[j][i] = MAX(ans[j][i], tempo_entrega[j]);
				}
			}
		}
	}
	return ans[nro_pedidos-1][nro_max_pizzas];
}

int main(){
	
	int i, j;
	int nro_pedidos;		// N
	int nro_max_pizzas;		// P
	int ans[max_nro_pedidos+1][max_nro_max_pizzas+1];
	int tempo_entrega[max_nro_pedidos+1], quantidade_pizzas_pedido[max_nro_pedidos+1];
	
	while(TRUE){
	
		scanf("%d", &nro_pedidos);
		// Interrompe execucao
		if(nro_pedidos == 0){
			break;
		}
		
		scanf("%d", &nro_max_pizzas);
		
		for(i=0 ; i<nro_pedidos ; i++){
			scanf("%d %d", &tempo_entrega[i], &quantidade_pizzas_pedido[i]);
			// Zera posicoes da matriz de resposta
			memset(&ans[i], 0, sizeof(ans[i]));
		}
		
		printf("%d min.\n", calcula(nro_max_pizzas, nro_pedidos, ans, quantidade_pizzas_pedido, tempo_entrega));
				
	}
	
}
