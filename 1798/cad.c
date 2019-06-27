#include <stdio.h>
#include <string.h>
#include <math.h>

int ci[1000]; // tamanho de cada cano
int vi[1000]; // valor de cada cano

int m[2001];

int main() {
int NC; // número de canos
int TC; // tamanho do cano
scanf("%d",&NC);
scanf("%d",&TC);
int i;
for (i=1;i<=NC;i++)
   scanf("%d%d",&ci[i],&vi[i]);
m[0] = 0;
int w;
for(w = 1; w <=TC; w++){
   m[w] = m[w-1];
   int j;
   for(j=0; j<NC; j++)
      if(ci[j] <= w)
	     if(m[w] < m[w-ci[j]] + vi[j])
		    m[w] = m[w-ci[j]]+ vi[j];
	}
printf("%d\n",m[TC]);
return 0;
}
