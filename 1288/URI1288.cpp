#include <stdio.h>

#define max_nro_projeteis 50
#define max_cap_carga_canhao 100
// Retorna o maior
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int calcula(int cap_carga_canhao, int nro_projeteis, int peso_projetil[max_nro_projeteis], int poder_destruicao[max_nro_projeteis], int res_castelo, int m[max_nro_projeteis+1][max_cap_carga_canhao+1]){
	
	int i,j;
	
	// Zera primeira linha
	for(i=0 ; i<=cap_carga_canhao ; i++)
		m[0][i] = 0;
		
	// Zera primeira coluna
	for(i=0 ; i<=nro_projeteis ; i++)
		m[i][0] = 0;
		
	for(i=1 ; i<=nro_projeteis ; i++){
		for(j=1 ; j<=cap_carga_canhao ; j++){
			if(peso_projetil[i] > j){
				m[i][j] = m[i-1][j];
			} else{
				m[i][j] = MAX(m[i-1][j], m[i-1][j-peso_projetil[i]] + poder_destruicao[i]);
			}
		}
	}
	
	if(m[nro_projeteis][cap_carga_canhao] >= res_castelo){
		return 1;
	} else{
		return 0;
	}
}

int main(){
	
	int i, casos_teste, nro_projeteis, x, y, poder_destruicao[max_nro_projeteis+1];
	int peso_projetil[max_nro_projeteis+1], cap_carga_canhao, res_castelo, m[max_nro_projeteis+1][max_cap_carga_canhao+1];
	scanf("%d", &casos_teste);
	
	while(casos_teste--)
	{
		scanf("%d", &nro_projeteis);
		
		//poder de destruicao   peso do projetil
		for(i=1 ; i<=nro_projeteis ; i++){
			scanf("%d %d", &poder_destruicao[i], &peso_projetil[i]);
		}
		
		scanf("%d %d", &cap_carga_canhao, &res_castelo);
		
		if(calcula(cap_carga_canhao, nro_projeteis, peso_projetil, poder_destruicao, res_castelo, m)){
			printf("Missao completada com sucesso\n");
		} else{
			printf("Falha na missao\n");
		}
	}
	return 0;
}
