    # -*- coding: utf-8 -*-
"""
Created on Thurs Jun 6 04:25:06 2024

@author: Jesus Alejandro Montes Aguila 
"""
import networkx as nx
import matplotlib.pyplot as plt
'''
Este código implementa un algoritmo de Dijkstra para encontrar el camino de menor resistencia entre vértices en un grafo y visualiza el grafo y el camino encontrado.

### Componentes principales:

1. Clase `Vertice`
   - Representa un nodo con vecinos (y su resistencia), estado de visita, vértice padre y distancia acumulada desde el inicio.

2. Clase `Grafica`
   - Maneja el conjunto de vértices y aristas.
   - Implementa el algoritmo de Dijkstra para encontrar el camino de menor resistencia.
   - Métodos para agregar vértices, aristas, encontrar el vértice no visitado con la menor distancia, imprimir resultados y obtener el camino más corto.

3. Función `dibujar_grafo`
   - Utiliza `networkx` y `matplotlib` para visualizar el grafo y resaltar el camino más corto encontrado.

El código crea un grafo, ejecuta Dijkstra desde el vértice 1 al 6, imprime los resultados y dibuja el grafo resaltando el camino encontrado.
'''
# Clase que representa un vértice del grafo
class Vertice:
    def __init__(self, i):
        # Identificador del vértice
        self.id = i
        # Lista de vecinos del vértice, donde cada vecino es un par (vértice, resistencia)
        self.vecinos = []
        # Indica si el vértice ha sido visitado durante el algoritmo de Dijkstra
        self.visitado = False
        # Vértice padre en el camino de menor resistencia
        self.padre = None
        # Distancia acumulada desde el vértice de inicio hasta el vértice actual
        self.distancia = float('inf')  # Representa la resistencia acumulada

    # Agrega un vecino al vértice
    def agregarVecino(self, v, resistencia):
        if not any(vecino[0] == v for vecino in self.vecinos):
            self.vecinos.append([v, resistencia])

# Clase que representa el grafo
class Grafica:
    def __init__(self):
        # Diccionario de vértices, donde cada clave es el id del vértice y el valor es una instancia de la clase Vertice
        self.vertices = {}

    # Agrega un vértice al grafo
    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    # Agrega una arista al grafo
    def agregarArista(self, a, b, resistencia):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, resistencia)
            self.vertices[b].agregarVecino(a, resistencia)

    # Devuelve el vértice con la distancia más corta no visitada
    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v

    # Imprime los valores finales de la gráfica
    def imprimirGrafica(self):
        for v in self.vertices:
            print(f"La resistencia acumulada del vertice {v} es {self.vertices[v].distancia} llegando desde {self.vertices[v].padre}")

    # Devuelve el camino de menor resistencia entre dos vértices
    def camino(self, a, b):
        camino = []
        actual = b
        while actual is not None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]

    # Ejecuta el algoritmo de Dijkstra en el grafo
    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = list(self.vertices.keys())

            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if not self.vertices[vecino[0]].visitado:
                        nueva_resistencia = self.vertices[actual].distancia + vecino[1]
                        if nueva_resistencia < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = nueva_resistencia
                            self.vertices[vecino[0]].padre = actual
                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)
        else:
            return False

# Función para dibujar el grafo con el camino resaltado
def dibujar_grafo(g, camino=None):
    G = nx.Graph()

    for vertice in g.vertices:
        G.add_node(vertice)
        for vecino in g.vertices[vertice].vecinos:
            G.add_edge(vertice, vecino[0], weight=vecino[1])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if camino:
        path_edges = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.show()

# Ejemplo de uso
g = Grafica()
g.agregarVertice(1)
g.agregarVertice(2)
g.agregarVertice(3)
g.agregarVertice(4)
g.agregarVertice(5)
g.agregarVertice(6)
g.agregarArista(1, 6, 14)  # 14 ohm
g.agregarArista(1, 2, 7)   # 7 ohm
g.agregarArista(1, 3, 9)   # 9 ohm
g.agregarArista(2, 3, 10)  # 10 ohm
g.agregarArista(2, 4, 15)  # 15 ohm
g.agregarArista(3, 4, 11)  # 11 ohm
g.agregarArista(3, 6, 2)   # 2 ohm
g.agregarArista(4, 5, 6)   # 6 ohm
g.agregarArista(5, 6, 9)   # 9 ohm

print("\n\nLa ruta con menor resistencia (Dijkstra) junto con su resistencia acumulada es:")
g.dijkstra(1)
camino, resistencia = g.camino(1, 4)
print(f"Camino: {camino}, Resistencia: {resistencia}")

print("\nLos valores finales de la gráfica son los siguientes:")
g.imprimirGrafica()

# Dibujar el grafo con el camino resaltado
dibujar_grafo(g, camino)
