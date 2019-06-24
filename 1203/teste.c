#include <stdio.h>
#define MAXR 101
#define MAXK 10010
int GRAU[MAXR],DP[MAXR][MAXK],POSSIVEL,REGIOES,PONTES;

int solve(int regiao,int restam){
    if (POSSIVEL){
        return 1;
    }
    if (restam < 0 || regiao > REGIOES){
        return 0;
    }
    if(restam == 0){
        POSSIVEL = 1;
        return DP[regiao][restam] = 1;
    }
    if(DP[regiao][restam] != -1){
        return DP[regiao][restam];
    }
    DP[regiao][restam] = solve(regiao+1,restam) || solve(regiao+1,restam - GRAU[regiao]);
    return DP[regiao][restam];
}

int main(){
    while(scanf("%d %d",&REGIOES,&PONTES) != EOF){
        POSSIVEL = 0;
    for(int i=1;i<=REGIOES;i++){
        GRAU[i] = 0;
        for(int j=0;j<=PONTES;j++){
            DP[i][j] = -1;
        }
    }
    for(int i=1;i<=PONTES;i++){
        int u,v;
        scanf("%d %d",&u,&v);
        GRAU[u]++;
        GRAU[v]++;
    }
    printf("%c\n", solve(1,PONTES) ? 'S' : 'N');
    }
    return 0;
}
