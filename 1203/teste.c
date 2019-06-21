#include <stdio.h>
#define MAXR 101
#define MAXK 10010
int grau[MAXR],dp[MAXR][MAXK],possivel,r,k;

int calcula(int regiao,int restam){
    if (possivel){
        return 1;
    }
    if (restam < 0 || regiao > r){
        return 0;
    }
    if(restam == 0){
        possivel = 1;
        return dp[regiao][restam] = 1;
    }
    if(dp[regiao][restam] != -1){
        return dp[regiao][restam];
    }
    dp[regiao][restam] = calcula(regiao+1,restam) || calcula(regiao+1,restam - grau[regiao]);
    return dp[regiao][restam];
}

int main(){
    while(scanf("%d %d",&r,&k) != EOF){
        possivel = 0;
    for(int i=1;i<=r;i++){
        grau[i] = 0;
        for(int j=0;j<=k;j++){
            dp[i][j] = -1;
        }
    }
    for(int i=1;i<=k;i++){
        int u,v;
        scanf("%d %d",&u,&v);
        grau[u]++;
        grau[v]++;
    }
    printf("%c\n", calcula(1,k) ? 'S' : 'N');
    }
    return 0;
}