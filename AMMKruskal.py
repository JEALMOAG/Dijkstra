
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:25:06 2024

@author: Jesus Alejandro Montes Aguila 
"""
'''
Componente, Conexion y Circuito. La clase Componente representa un componente electrónico
con un nombre y un costo. La clase Conexion representa una conexión entre dos componentes
electrónicos con un costo asociado. La clase Circuito representa un circuito electrónico compuesto por componentes y conexiones.

La función kruskal_minimo devuelve el circuito óptimo de mínimo costo, mientras que la
función kruskal_maximo devuelve el circuito óptimo de máximo costo.

En el ejemplo de uso, se crean componentes electrónicos y conexiones entre ellos con 
costos asociados. Luego, se crea un objeto Circuito y se llama a las funciones kruskal_minimo 
y kruskal_maximo para encontrar el circuito óptimo de mínimo y máximo costo respectivamente.

El resultado muestra el circuito óptimo de mínimo costo y el circuito óptimo de máximo costo, 
con las conexiones entre los componentes electrónicos y sus respectivos costos.
'''
import heapq

# Clase que representa un componente del circuito
class Componente:
    def __init__(self, nombre, costo):
        self.nombre = nombre  # Nombre del componente
        self.costo = costo    # Costo asociado al componente

# Clase que representa una conexión entre dos componentes
class Conexion:
    def __init__(self, componente1, componente2, costo):
        self.componente1 = componente1  # Primer componente de la conexión
        self.componente2 = componente2  # Segundo componente de la conexión
        self.costo = costo              # Costo de la conexión

# Clase que representa el circuito completo
class Circuito:
    def __init__(self, componentes, conexiones):
        self.componentes = componentes    # Lista de todos los componentes del circuito
        self.conexiones = conexiones      # Lista de todas las conexiones entre componentes

    # Método para encontrar el árbol de expansión mínima utilizando Kruskal
    def kruskal_minimo(self):
        mst = []             # Aquí se almacenará el árbol de expansión mínima
        visitados = set()    # Conjunto para almacenar los componentes visitados
        heap = [(conexion.costo, conexion.componente1, conexion.componente2) for conexion in self.conexiones]
        heapq.heapify(heap)  # Convertir la lista en un heap (cola de prioridad)

        while heap:
            costo, componente1, componente2 = heapq.heappop(heap)  # Obtener la conexión de menor costo
            if componente1 not in visitados or componente2 not in visitados:
                mst.append((componente1, componente2, costo))  # Agregar la conexión al árbol de expansión mínima
                visitados.add(componente1)  # Marcar componente1 como visitado
                visitados.add(componente2)  # Marcar componente2 como visitado

        return mst

    # Método para encontrar el árbol de expansión máxima utilizando Kruskal
    def kruskal_maximo(self):
        mst = []             # Aquí se almacenará el árbol de expansión máxima
        visitados = set()    # Conjunto para almacenar los componentes visitados
        heap = [(-conexion.costo, conexion.componente1, conexion.componente2) for conexion in self.conexiones]
        heapq.heapify(heap)  # Convertir la lista en un heap (cola de prioridad)

        while heap:
            costo, componente1, componente2 = heapq.heappop(heap)  # Obtener la conexión de mayor costo
            if componente1 not in visitados or componente2 not in visitados:
                mst.append((componente1, componente2, -costo))  # Agregar la conexión al árbol de expansión máxima
                visitados.add(componente1)  # Marcar componente1 como visitado
                visitados.add(componente2)  # Marcar componente2 como visitado

        return mst

# Ejemplo de uso
componentes = [
    Componente('R1', 10),
    Componente('R2', 20),
    Componente('C1', 30),
    Componente('C2', 40),
    Componente('IC1', 50)
]

conexiones = [
    Conexion(componentes[0], componentes[1], 5),
    Conexion(componentes[0], componentes[2], 10),
    Conexion(componentes[1], componentes[2], 15),
    Conexion(componentes[1], componentes[3], 20),
    Conexion(componentes[2], componentes[3], 25),
    Conexion(componentes[2], componentes[4], 30),
    Conexion(componentes[3], componentes[4], 35)
]

circuito = Circuito(componentes, conexiones)

print("Circuito óptimo de mínimo costo:")
for componente1, componente2, costo in circuito.kruskal_minimo():
    print(f"{componente1.nombre} - {componente2.nombre} : {costo}")

print("\nCircuito óptimo de máximo costo:")
for componente1, componente2, costo in circuito.kruskal_maximo():
    print(f"{componente1.nombre} - {componente2.nombre} : {costo}")
