#include <bits/stdc++.h>
using namespace std;
char table[8][8];
bool visited[8][8];

void paint(int row, int col) {
  int i, j;
  for (i = 0; i < 8; i++) {
    visited[row][i] = true;
    visited[i][col] = true;
  }
  j = col;
  for (i = row; i >= 0 && j >= 0; i--, j--) {
    visited[i][j] = true;
  }
  j = col;
  for (i = row; i < 8 && j < 8; i++, j++) {
    visited[i][j] = true;
  }
  j = col;
  for (i = row; i >= 0 && j < 8; i--, j++) {
    visited[i][j] = true;
  }
  j = col;
  for (i = row; i < 8 && j >= 0; i++, j--) {
    visited[i][j] = true;
  }
}

void printTable(){
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      /*if (table[i][j] != 'q') {
        cout << '-';
      } else cout << table[i][j] ;
      */ cout << visited[i][j] ;
    }
    cout << endl;
  }
}

bool bfs(int s) {
  int queens = 0;
  int rows = 0; // inicia en la fila 0
  queue<int> q; // columnas
  q.push(s); // inserta la columna donde se posiciona la 1era reina
  table[rows][s] = 'q';
  visited[rows][s] = true;
  paint(rows, s); // pinta todos los ataques de la reina en esa posicion
  cout << "--------" << endl;
  cout << "row : " << rows << ", col : " << s << endl;
  printTable();
  cout << "--------" << endl;
  while (!q.empty()) {
    int n = q.front(); // siguiente elemento de la cola
    q.pop(); // lo saca de la cola
    paint(rows,n); //pinta el elemento que acaba de sacar
    queens++;
    cout << "--------" << endl;
    cout << "row : " << rows << ", col : " << n << endl;
    printTable();
    cout << "--------" << endl;
    if (queens == 8) return true; // caso base, ya posicionó todas las reinas
    for (int j = 0; j < 8; j++) { // busca una columna donde pueda posicionar la siguiente
      if (!visited[rows+1][j]) {
        q.push(j); // lo analiza la siguiente iteración
        visited[rows+1][j] = true; // visitado
        //paint(rows+1,j); // pinta movimientos posibles de esa ficha
        //queens++;
        table[rows+1][j] = 'q';
      }
    }
    rows++; // pasa de fila
  }
  return false;
}

int main(void){
  memset(visited, 0, sizeof visited);
  memset(table, '-', sizeof table);
  /*if (bfs(0)) { // busca una solución
    printTable();
  } else cout << "no se encontró solución" << endl;*/
  paint(5,4);
  printTable();
  return 0;
}
