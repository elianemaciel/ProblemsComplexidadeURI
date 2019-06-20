#include <stdio.h>

#define max_valor_final_compra 100000	//N
#define max_nro_moedas 1000				//M

int calcula(int nro_moedas, int valor_moedas[max_nro_moedas], int ans[max_valor_final_compra], int valor_final_compra){
	
	int i, j;
	// Caso basico
	ans[0] = 1;
	
	for(j=0 ; j<nro_moedas ; j++){
		for(i=valor_final_compra ; i>=valor_moedas[j] ; i--){
			// Operacao binaria 'ou' no vetor resposta
			ans[i] = ans[i] | ans[i-valor_moedas[j]];
		}
	}
	
	if(ans[valor_final_compra] == 1){
		return 1;
	} else{
		return 0;
	}
	
}

int main(){
	
	int i, valor_final_compra, nro_moedas, valor_moedas[max_nro_moedas], ans[max_valor_final_compra];
	
	scanf("%d %d", &valor_final_compra, &nro_moedas);
	
	for(i=0 ; i<nro_moedas ; i++){
		scanf("%d", &valor_moedas[i]);
	}
	
	if(calcula(nro_moedas, valor_moedas, ans, valor_final_compra) ? printf("S\n") : printf("N\n"));
}
