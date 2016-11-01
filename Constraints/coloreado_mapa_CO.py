CHO = "Choco"
VAC = "Valle del Cauca"
CAU = "Cauca"
NAR = "Narino"
PUT = "Putumayo"
AMA = "Amazonas"
ANT = "Antioquia"
RIS = "Risaralda"
CAL = "Caldas"
QUI = "Quindio"
TOL = "Tolima"
VAU = "Vaupes"
GUA = "Guajira"
GUV = "Guaviare"
CAQ = "Caqueta"

colombia = {
            CHO:{RIS},
            RIS:{CHO,VAU},
            VAU:{RIS}
           }

colors = {'r','g','b','y'}

def check_valid(graph):
    for node,nexts in graph.iteritems():
        assert(nexts) #No hay nodos unicos
        assert(node not in nexts) #No hay nodos referenciandose a si mismos
        for next in nexts:
            assert(next in graph and node in graph[next]) #A enlazado a B implica B enlazado a A

class MapColor(object):
    def __init__(self,graph,colors):
        check_valid(graph)
        self.graph = graph
        nodes = list(self.graph.keys())
        self.node_colors = {node:None for node in nodes}
        self.domains = {node:set(colors) for node in nodes}

    def solve(self):
        uncolores_nodes = [n for n,c in self.node_colors.iteritems() if c is None]
        if not uncolores_nodes:
            print(self.node_colors) # imprime el color final de cada nodo
            return True
        node = uncolores_nodes[0]
        #print "dominio para " + node + ": " + str(self.domains[node])
        for color in self.domains[node]:  #Todo el for es el BackTracking del problema
            if all(color != self.node_colors[n] for n in self.graph[node]):
                self.set_color(node,color)
                self.remove_from_domains(node, color)
                if self.solve():
                    return True
                self.set_color(node,None)
                self.add_to_domains(node,color) #Finaliza el BackTracking
        return False

    def set_color(self,key,color):
        self.node_colors[key] = color

    def remove_from_domains(self,key,color):
        for node in self.graph[key]:
            if(color in self.domains[node]):
                self.domains[node].remove(color)
    def add_to_domains(self,key,color):
        for node in self.graph[key]:
            self.domains[node].add(color)

if __name__ == "__main__":
    algo = MapColor(colombia,colors)
    algo.solve()
