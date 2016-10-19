import sys
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import heapq
from functools import total_ordering

class Point(): # para manejar las coordenadas

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def dist(self, p):
        nx = self.x - p.x
        ny = self.y - p.y
        return math.sqrt(nx * nx + ny * ny)

@total_ordering
class Node():

    def __init__(self, id, point, neighbors = []):
        self.id = id
        self.point = point
        self.neighbors = neighbors

    def createNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def getEdge(self, neighbor):
        return self.point.dist(neighbor.point)

    def connectWithAll(self, nodes):
        for i in range(0,len(nodes)):
            tmp = nodes[:]
            tmp.remove(nodes[i])
            self.neighbors = tmp

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.point.dist(other.point) == other.point.dist(self.point)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.point.dist(other.point) < other.point.dist(self.point)
        return NotImplemented

class Graph():

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

        for node in nodes :
            for neighbor in node.neighbors :
                self.edges.append((node,neighbor,node.getEdge(neighbor)))

def PlotHelper(graph):
    inf = float('inf')
    x = []
    y = []
    info = [-inf,inf,-inf,inf] # max x, min x, max y, min y
    size = len(graph)
    for i in range(0,size + 1):
        x_tmp = graph[i % size].point.x
        y_tmp = graph[i % size].point.y
        info = [max(info[0], x_tmp), min(info[1], x_tmp), min(info[3], y_tmp), max(info[2], y_tmp)]
        x.append(x_tmp)
        y.append(y_tmp)
    return x, y, info

def PlotSolution(graph, name):
    x,y, info = PlotHelper(graph)
    plt.plot(x, y, "ro")
    plt.plot(x, y)
    Xrange = [(info[1] - 1) * 3, (info[0] + 1) * 3]
    Yrange = [(info[3] - 1)  * 3, (info[2] + 1) * 3]
    plt.axis([Xrange[0], Xrange[1], Yrange[0], Yrange[1]])

    for i in range(0,len(x)):
        plt.text(x[i], y[i], i)

    plt.title(name)
    plt.show()

def init(path):
    fo = open(sys.argv[1], 'r') # abre el archivo como lectura
    nline = 0
    while nline < 6 :
        line = fo.readline().strip()
        nline += 1
    line = fo.readline().strip()
    nodes =  []
    while line != "EOF":
        n, x, y = line.split(" ")
        tx = Point(int(x), int(y))
        nt = Node(int(n), tx)
        nodes.append(nt)
        line = fo.readline().strip()
    return nodes

def init_tour(tours):
    random.shuffle(tours)
    return tours

def objective_function(nodes):
    ans = 0
    ss = len(nodes)
    for i in range(0, ss):
        ans += nodes[i].point.dist(nodes[(i + 1) % ss].point)
    return ans

def swap(v):
    r1 = random.randint(0,len(v)-1)
    while True:
        r2 = random.randint(0,len(v)-1)
        if r2 != r1:
            break

    v[r1],v[r2] = v[r2],v[r1]
    return v

def simulatedAnnealing(graph, to, ts, r, mer): #grafo, T inicial, T final, % enfriamiento, iteraciones

    best = init_tour(graph)
    best_score = objective_function(best)
    ans = best
    cost_ans = best_score

    t = to

    while t > ts:
        for _ in range(0,mer):
            new_graph = swap(best)
            new_cost = objective_function(new_graph)
            delta = new_cost - best_score
            if delta < 0:
                best = new_graph
                best_score = new_cost
            else:
                p = np.exp(-delta / t)
                if np.random.rand(0, 1) < p:
                    best = new_graph
                    best_score = new_cost
        if(best_score < cost_ans):
            cost_ans = best_score
            ans = best

        t *= r
    return (cost_ans, ans)

def hillClimbing(max_evaluations, graph):

    best = init_tour(graph)
    best_score = objective_function(best)
    num_evaluations = 1

    while num_evaluations < max_evaluations:
        move_made = False

        while(True):
            next = swap(best)
            if num_evaluations >= max_evaluations:
                break

            next_score = objective_function(next)
            num_evaluations += 1
            if next_score < best_score:
                best = next
                best_score = next_score
                move_made = True
                break

        if not move_made:
            break

    return (best_score,best)


def A(graph):
    q = [] # costo, nodos por visitar, nodos visitados

    for node in graph.nodes:
        q.append([ 0.0, node.neighbors, [node] ])

    heapq.heapify(q)
    seen = set()

    while True:
        curr = heapq.heappop(q)

        if (len(curr[1]) == 0): # no tiene mas nodos por visitar
            u = curr[2][0]
            v = curr[2][len(curr[2]) - 1]
            idx_u = graph.nodes.index(u)
            idx_v = graph.nodes.index(v)
            curr[0] += graph.nodes[idx_u].getEdge(graph.nodes[idx_v])
            return curr[0],curr[2]
        from_ = curr[2][len(curr[2]) - 1]
        for node in curr[1]: # nodos por visitar
            idx_from_ = graph.nodes.index(from_)
            idx_node = graph.nodes.index(node)
            d = graph.nodes[idx_from_].getEdge(graph.nodes[idx_node])
            missing = curr[1][:]
            missing.remove(node)
            visited = curr[2][:]
            visited.append(node)
            heapq.heappush(q, [d + curr[0] + len(missing), missing, visited])
            # Es el mismo dijkstra pero con una funcion objetivo de mas para sumar al costo


def dijkstra(graph, f, t):#size_nodes):
    q = [] # costo, nodos por visitar, nodos visitados

    for node in graph.nodes:
        q.append([ 0.0, node.neighbors, [node] ])

    heapq.heapify(q)
    seen = set()

    while True:
        curr = heapq.heappop(q)

        if (len(curr[1]) == 0): # no tiene mas nodos por visitar
            u = curr[2][0]
            v = curr[2][len(curr[2]) - 1]
            idx_u = graph.nodes.index(u)
            idx_v = graph.nodes.index(v)
            curr[0] += graph.nodes[idx_u].getEdge(graph.nodes[idx_v])
            return curr[0],curr[2]
        from_ = curr[2][len(curr[2]) - 1]
        for node in curr[1]: # nodos por visitar
            idx_from_ = graph.nodes.index(from_)
            idx_node = graph.nodes.index(node)
            d = graph.nodes[idx_from_].getEdge(graph.nodes[idx_node])
            missing = curr[1][:]
            missing.remove(node)
            visited = curr[2][:]
            visited.append(node)
            heapq.heappush(q, [d + curr[0], missing, visited])
    """
        if curr not in seen:
            seen.add(curr)
            path = (curr, path)
            #if len(seen) == size_nodes:
            if curr == t :
                return (cost, path)

            # por cada uno de los vecinos de v1
            idx_node = graph.nodes.index(curr)
            for neighbor in graph.nodes[idx_node].neighbors :
                if neighbor not in seen:
                    c = curr.getEdge(neighbor)
                    heapq.heappush(q, (cost + c, neighbor, path))

    return float("inf")"""

def ShowGraph(graph):
    for i in graph:
        print (i.id),
    print ()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    nodes = init(sys.argv[1]) #inicializa el grafo

    #-------------Hill Climbing-----------------
    hillClimbing_solution = hillClimbing(len(nodes), nodes)
    print ("best score in hillClimbing : " , hillClimbing_solution[0])
    PlotSolution(hillClimbing_solution[1],"hillClimbing")
    ShowGraph(hillClimbing_solution[1])

    #-----------Simulated Annealing---------------
    simulatedAnnealing_solution = simulatedAnnealing(nodes, 500, 10, 0.997, 20)
    print ("best score in simulatedAnnealing : " , simulatedAnnealing_solution[0])
    PlotSolution(simulatedAnnealing_solution[1],"Annealing")
    ShowGraph(simulatedAnnealing_solution[1])

    #---------------Greedy-----------------

    for node in nodes :
        node.connectWithAll(nodes)

    graph = Graph(nodes)

    dijkstra_solution = dijkstra(graph,nodes[0], nodes[len(nodes)-1])#len(nodes))
    print ("Dijkstra : ", dijkstra_solution[0])

    #---------------A*-------------------

    A_solution = A(graph)
    print ("A* : ", A_solution[0])
