class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
 
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
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecha, valor)
 
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)
 
    def _buscar_rec(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_rec(nodo.izquierda, valor)
        return self._buscar_rec(nodo.derecha, valor)

if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda() 
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    # Buscar un valor y mostrar el resultado

    resultado = arbol.buscar(70)
    if resultado:
        print(f"Se encontró el nodo con valor: {resultado.valor}")
    else:
        print("No se encontró el valor en el árbol")