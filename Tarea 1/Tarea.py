from graphviz import Digraph
import os

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                print(f"Estudiante con carnet {carnet} eliminado.")
                return True
            actual = actual.siguiente
        print("No se encontró ningún estudiante con ese carnet.")
        return False

    def mostrar_lista(self):
        if not self.cabeza:
            print("None")
            return
        actual = self.cabeza
        print("None <- ", end="")
        while actual:
            print(f"[{actual.nombre} {actual.apellido} ({actual.carnet})]", end="")
            if actual.siguiente:
                print(" <-> ", end="")
            actual = actual.siguiente
        print(" -> None")

    def generar_png(self):
        print("Se guardará en:", os.getcwd())

        dot = Digraph("ListaDoble", format="png")
        dot.attr(rankdir="LR")

        actual = self.cabeza
        contador = 0
        nodos = []

        while actual:
            nombre_nodo = f"N{contador}"
            etiqueta = f"{actual.nombre}\n{actual.apellido}\n{actual.carnet}"
            dot.node(nombre_nodo, etiqueta)
            nodos.append(nombre_nodo)
            actual = actual.siguiente
            contador += 1

        for i in range(len(nodos) - 1):
            dot.edge(nodos[i], nodos[i+1])
            dot.edge(nodos[i+1], nodos[i])

        dot.render("lista_doble", view=True)


def menu():
    lista = Lista()

    while True:
        print("\n--- MENÚ LISTA DOBLEMENTE ENLAZADA ---")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2']:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")

            if opcion == '1':
                lista.insertar_al_principio(nombre, apellido, carnet)
            else:
                lista.insertar_al_final(nombre, apellido, carnet)

            print("Nodo insertado con éxito.")
            lista.generar_png()

        elif opcion == '3':
            valor = input("Ingrese el carnet del estudiante a eliminar: ")
            lista.eliminar_por_valor(valor)
            lista.generar_png()

        elif opcion == '4':
            print("\nEstado actual de la lista:")
            lista.mostrar_lista()

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()