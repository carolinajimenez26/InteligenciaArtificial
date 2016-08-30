#include <bits/stdc++.h>
#define n 8
using namespace std;

bool valido ( int vec[n] , int k){
    for ( int i = 0 ; i<k ; i++){
        if ((vec[i]== vec[k] ) || ( abs ( vec[i]-vec[k] ) ==  abs ( i-k))){
               return false;
        }
   }
   return true;
}


bool Reinas ( int solucion[n] , int col ){
 if ( col >= n ) return true;

 bool exito = false;
 solucion[col]=0;

 while (( solucion[col] < n  ) && (exito == false )){
   solucion[col] = solucion[col]+1 ;

   if ( valido ( solucion , col )==true) {
        if (col <= n ){
          exito = Reinas(solucion , col+1 );  // LLAMADO RECURSIVO
        }
        else {
          exito = true ;
        }
   }

  }

   return exito;
}



int main(int argc, char *argv[]){
	int Nreinas[n];
	for (int i=0; i<n ;i++){
	    Nreinas[i]=-1;

	}

	Reinas(Nreinas,0);


	for (int i=0; i<n ;i++){
	   cout<<"("<<Nreinas[i]<<","<<i+1<<")"<<endl;

	}


	cout<<"MATRIZ DE REINAS"<<endl;

	int aviso=1;
	for (int i=0 ; i<n ; i++){
	    for(int j= 0 ; j<n ; j++){
		    if(aviso==Nreinas[j]){
		        cout<<"Q";

		      }
			else{
				cout<<"*";
			}

		}
		aviso=aviso+1;
		cout<<endl;
	}
    return 0;
}
