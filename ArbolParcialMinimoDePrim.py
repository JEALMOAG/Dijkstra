
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:25:06 2024

@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un sistema de gestión de presupuestos que asigna dinero
a diferentes necesidades y subnecesidades según su prioridad y costo. Utiliza
una estructura de datos de cola de prioridad (heapq) para procesar las asignaciones
de manera eficiente, asegurando que las necesidades más prioritarias reciban financiamiento primero.'''
import heapq  # Importa el módulo heapq para manejar colas de prioridad (heaps)

# Clase que representa una necesidad
class Necesidad:
    def __init__(self, nombre, prioridad, costo):
        self.nombre = nombre  # Nombre de la necesidad
        self.prioridad = prioridad  # Prioridad de la necesidad
        self.costo = costo  # Costo de la necesidad
        self.asignado = 0  # Dinero asignado a la necesidad
        self.subnecesidades = []  # Lista de subnecesidades

    # Agrega una subnecesidad a la necesidad actual
    def agregar_subnecesidad(self, subnecesidad):
        self.subnecesidades.append(subnecesidad)

# Clase que representa el presupuesto
class Presupuesto:
    def __init__(self, dinero_disponible):
        self.dinero_disponible = dinero_disponible  # Dinero disponible para el presupuesto
        self.necesidades = {}  # Diccionario de necesidades

    # Agrega una necesidad al presupuesto
    def agregar_necesidad(self, nombre, prioridad, costo):
        if nombre not in self.necesidades:
            self.necesidades[nombre] = Necesidad(nombre, prioridad, costo)

    # Agrega una subnecesidad a una necesidad existente
    def agregar_subnecesidad(self, nombre_necesidad, nombre_subnecesidad, prioridad, costo):
        if nombre_necesidad in self.necesidades:
            subnecesidad = Necesidad(nombre_subnecesidad, prioridad, costo)
            self.necesidades[nombre_necesidad].agregar_subnecesidad(subnecesidad)

    # Asigna dinero a las necesidades basándose en la prioridad y el costo
    def asignar_dinero(self):
        mst = []  # Lista para almacenar las asignaciones finales
        visitados = set()  # Conjunto de necesidades ya visitadas
        heap = []  # Lista de tuplas para la cola de prioridad

        # Crear una lista de tuplas con la estructura (prioridad, nombre, costo)
        for necesidad in self.necesidades.values():
            heap.append((necesidad.prioridad, necesidad.nombre, necesidad.costo))
            for subnecesidad in necesidad.subnecesidades:
                heap.append((subnecesidad.prioridad, subnecesidad.nombre, subnecesidad.costo))

        # Convertir la lista en una cola de prioridad (heap)
        heapq.heapify(heap)

        # Mientras haya dinero disponible y necesidades por asignar
        while heap and self.dinero_disponible > 0:
            # Obtener la necesidad con mayor prioridad (menor valor numérico)
            prioridad, nombre, costo = heapq.heappop(heap)
            if nombre not in visitados:
                visitados.add(nombre)
                # Asignar dinero a la necesidad si hay suficiente disponible
                if costo <= self.dinero_disponible:
                    if nombre in self.necesidades:
                        self.necesidades[nombre].asignado = costo
                    else:
                        for necesidad in self.necesidades.values():
                            for subnecesidad in necesidad.subnecesidades:
                                if subnecesidad.nombre == nombre:
                                    subnecesidad.asignado = costo
                    self.dinero_disponible -= costo
                    mst.append((nombre, costo))
                else:
                    # Asignar el dinero restante si no es suficiente para cubrir todo el costo
                    if nombre in self.necesidades:
                        self.necesidades[nombre].asignado = self.dinero_disponible
                    else:
                        for necesidad in self.necesidades.values():
                            for subnecesidad in necesidad.subnecesidades:
                                if subnecesidad.nombre == nombre:
                                    subnecesidad.asignado = self.dinero_disponible
                    mst.append((nombre, self.dinero_disponible))
                    self.dinero_disponible = 0

        return mst

# Ejemplo de uso
presupuesto = Presupuesto(1000)  # Crear un presupuesto con 1000 unidades de dinero

# Agregar necesidades al presupuesto
presupuesto.agregar_necesidad('Alimentación', 1, 300)
presupuesto.agregar_necesidad('Transporte', 2, 200)
presupuesto.agregar_necesidad('Material de estudio', 3, 150)
presupuesto.agregar_necesidad('Ocio', 4, 100)

# Agregar subnecesidades a las necesidades existentes
presupuesto.agregar_subnecesidad('Alimentación', 'Desayuno', 1, 100)
presupuesto.agregar_subnecesidad('Alimentación', 'Almuerzo', 1, 150)
presupuesto.agregar_subnecesidad('Alimentación', 'Cena', 1, 50)
presupuesto.agregar_subnecesidad('Transporte', 'Gasolina', 2, 100)
presupuesto.agregar_subnecesidad('Transporte', 'Mantenimiento', 2, 100)
presupuesto.agregar_subnecesidad('Material de estudio', 'Libros', 3, 100)
presupuesto.agregar_subnecesidad('Material de estudio', 'Papelería', 3, 50)

# Asignar dinero a las necesidades basándose en la prioridad y el costo
asignaciones = presupuesto.asignar_dinero()
print("Asignaciones de dinero:")
for nombre, costo in asignaciones:
    print(f"{nombre}: {costo}")
