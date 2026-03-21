import csv
import os
from graphviz import Digraph

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)
    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_rec(nodo.der, valor)
        else:
            print("El valor ya existe en el árbol.")
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)
    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izq, valor)
        else:
            return self._buscar_rec(nodo.der, valor)
    def eliminar(self, valor):
        self.raiz = self._eliminar_rec(self.raiz, valor)
    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izq = self._eliminar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_rec(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            sucesor = self._min_valor(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar_rec(nodo.der, sucesor.valor)
        return nodo
    def _min_valor(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual
    def cargar_csv(self, ruta):
        if not os.path.exists(ruta):
            print("Archivo no encontrado.")
            return
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    try:
                        self.insertar(int(valor))
                    except ValueError:
                        print(f"Valor inválido en CSV: {valor}")
    def generar_graphviz(self, nombre_archivo="arbol"):
        dot = Digraph()
        self._agregar_nodos(dot, self.raiz)
        dot.render(nombre_archivo, format="png", cleanup=True)
        print(f"Árbol exportado como {nombre_archivo}.png")
    def _agregar_nodos(self, dot, nodo):
        if nodo is not None:
            dot.node(str(nodo.valor))
            if nodo.izq:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                self._agregar_nodos(dot, nodo.izq)
            if nodo.der:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                self._agregar_nodos(dot, nodo.der)
def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\n--- ÁRBOL BINARIO DE BÚSQUEDA ---")
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Cargar desde archivo CSV")
        print("5. Generar gráfico (Graphviz)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            try:
                valor = int(input("Ingrese el número a insertar: "))
                arbol.insertar(valor)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "2":
            try:
                valor = int(input("Ingrese el número a buscar: "))
                encontrado = arbol.buscar(valor)
                if encontrado:
                    print("El número se encuentra en el árbol.")
                else:
                    print("El número NO se encuentra en el árbol.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "3":
            try:
                valor = int(input("Ingrese el número a eliminar: "))
                arbol.eliminar(valor)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "4":
            ruta = input("Ingrese la ruta del archivo CSV: ")
            arbol.cargar_csv(ruta)
        elif opcion == "5":
            nombre = input("Nombre del archivo de salida (sin extensión): ")
            arbol.generar_graphviz(nombre)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__":
    menu()
