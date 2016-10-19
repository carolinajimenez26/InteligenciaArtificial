## Algoritmos para resolver el problema del viajero (TSP).

### Recocido Simulado:
Recocido simulado recibe 5 cosas, un grafo, una temperatura inicial, una temperatura final, la velocidad de enfriamiento y el número de mezclas a realizar.
Para solucionar TSP con recocido simulado, se toma el grafo y se busca una solución aleatoria con init_tour() para que sea la solución inicial, con  objective_function() se calcula el costo de esta solución.
Mientras que no se llegue a la temperatura final se van a hacer tantas “mezclas” como haya recibido la función de recocido simulado, en cada una de estas mezclas se hará lo siguiente:
Se creara con  swap() una solución vecina de nuestra solución actual (de la mejor solución hasta el momento).
Se calcula el costo de esta nueva solución.
Se calcula delta = new_cost - best_score y si este delta es negativo, la solución vecina pasa a ser la nueva mejor solución, de lo contrario se someterá a una probabilidad.
Termina esta mezcla si el costo de la nueva solución es menor que el costo de la solución anterior, el costo de la nueva solución pasara a ser el nuevo mejor costo.
Se actualiza la temperatura con la velocidad de enfriamiento.
Se retornara el mejor costo y la mejor solución.

### Ascenso a la montaña:
Ascenso a la montaña recibe el número máximo de iteraciones que queremos hacer, para no quedarnos buscando infinitamente un óptimo local. La función objetivo y la inicialización de la primera solución es igual que en recocido simulado. En cada iteración se analiza si se excedió el límite de iteraciones, y si es así, rompe el ciclo, retornando alguna solución. Analiza también en cada iteración si la función objetivo de una nueva solución aleatoria es menor a la que se tiene en ese moemnto, y si es así, actualiza la nueva mejor solución.
El algoritmo retorna el valor del óptimo local encontrado y la secuencia de cómo deben ser visitados los nodos.

### Clases y funciones de las implementacines:

### Clases :

#### Class Point():

Esta clase se hizo para el manejo de las coordenadas de cada nodo, tiene su posición en el eje X y en el eje Y.

- **dist(self, p):**  Con este método se calcula la distancia que hay entre este  punto y otro punto.

#### Class Node():

Esta clase permite instancias nodos, con su identificador y sus coordenadas.

- **createNeighbor(self, neighbor):** añade un vecino a un nodo.

- **getEdge(self, neighbor):** retorna el valor del arco entre dos nodos

- **connectWithAll(self, nodes):** conecta cada uno de los nodos con todos los otros, sin incluirse.

#### Class Graph():

Esta clase permite tener almacenado todos los nodos y aristas de un grafo. Se construye a partir de un conjunto de nodos.


### Funciones:

- **init_tour(tours):** Esta función permite tener una solución inicial aleatoria.

- **init(path):** En esta función, se recibe la instancia de TSP y se abre en modo lectura, se ignoran las primeras 6 líneas dado a que solo son información del grafo, se leen las líneas que hay desde la 7 hasta que haya un fin de archivo, dividimos cada línea en 3 partes,  cada una de estas corresponden a el identificador de nodo y sus coordenadas en X y en Y. Se crean instancias de Point y de Node con estos datos y se guarda en una lista.

- **objective_function(nodes):** En esta función se calcula la distancia que hay entre cada nodo.

- **swap(v):** En esta function se genera un solución vecina de la major solución actual, solamente se intercambian dos nodos.

- **PlotSolution(graph):** Utiliza la librería _Matplotlib_, la cual permite hacer gráficos de forma sencilla, simplemente definiendo todos los puntos que van a ser graficados y datos adicionales como nombres de los ejes y título del gráfico.

- **PlotHelper(graph):** _Matplotlib_ recibe como parámetros para graficar dos listas, uno con las coordenadas de x y otra con las de y. Recorremos cada uno de los nodos del grafo y sacamos sus coordenadas; además, retornamos cuáles son los puntos menores y mayores del grafo, para tener el rango que debemos graficar.

- **ShowGraph(graph):** imprime cada uno de los nodos del grafo.


____________________________________
Presentado por:

Angie Vanessa Penagos Rios
Carolina Jiménez Gómez
