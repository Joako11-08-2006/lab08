from collections import deque

class NodoArbol:
    """Clase para representar un nodo en un árbol binario."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    """Clase para representar un árbol binario."""
    def __init__(self):
        self.raiz = None
    
    def construir_arbol_desde_lista(self, lista):
        """Construye un árbol binario a partir de una lista de valores en orden de nivel."""
        if not lista:
            return
        
        self.raiz = NodoArbol(lista[0])
        cola = deque([self.raiz])
        i = 1
        
        while cola and i < len(lista):
            nodo_actual = cola.popleft()
            
            # Hijo izquierdo
            if i < len(lista) and lista[i] is not None:
                nodo_actual.izquierda = NodoArbol(lista[i])
                cola.append(nodo_actual.izquierda)
            i += 1
            
            # Hijo derecho
            if i < len(lista) and lista[i] is not None:
                nodo_actual.derecha = NodoArbol(lista[i])
                cola.append(nodo_actual.derecha)
            i += 1
    
    def imprimir_estructura(self):
        """Imprime la estructura del árbol en forma visual."""
        self._imprimir_estructura_recursivo(self.raiz, "", True)
    
    def _imprimir_estructura_recursivo(self, nodo, prefijo, es_ultimo):
        """Función auxiliar recursiva para imprimir la estructura del árbol."""
        if nodo is not None:
            print(prefijo + ("└── " if es_ultimo else "├── ") + str(nodo.valor))
            
            # Prepara el prefijo para los hijos
            nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
            
            # Imprime el hijo derecho primero, luego el izquierdo
            if nodo.derecha or nodo.izquierda:
                self._imprimir_estructura_recursivo(nodo.derecha, nuevo_prefijo, nodo.izquierda is None)
                self._imprimir_estructura_recursivo(nodo.izquierda, nuevo_prefijo, True)


def ancestro_comun_mas_cercano(raiz, p, q):
    """
    Encuentra el ancestro común más cercano (LCA) de dos nodos en un árbol binario.
    
    Args:
        raiz: La raíz del árbol binario.
        p: El valor del primer nodo.
        q: El valor del segundo nodo.
        
    Returns:
        El valor del nodo que es el ancestro común más cercano, o None si no existe.
    """
    resultado = _buscar_ancestro(raiz, p, q)
    return resultado.valor if resultado else None


def _buscar_ancestro(raiz, p, q):
    """
    Función auxiliar recursiva para encontrar el ancestro común más cercano.
    
    Args:
        raiz: La raíz del árbol o subárbol actual.
        p: El valor del primer nodo.
        q: El valor del segundo nodo.
        
    Returns:
        El nodo que es el ancestro común más cercano, o None si no existe.
    """
    # Caso base: si la raíz es None o encontramos uno de los nodos
    if raiz is None:
        return None
    
    if raiz.valor == p or raiz.valor == q:
        return raiz
    
    # Buscar en los subárboles izquierdo y derecho
    izquierda = _buscar_ancestro(raiz.izquierda, p, q)
    derecha = _buscar_ancestro(raiz.derecha, p, q)
    
    # Si encontramos nodos en ambos subárboles, entonces la raíz actual es el LCA
    if izquierda and derecha:
        return raiz
    
    # Si solo encontramos en un subárbol, ese resultado es el LCA o un ancestro del LCA
    return izquierda if izquierda else derecha


def existe_nodo(raiz, valor):
    """
    Verifica si un nodo con el valor dado existe en el árbol.
    
    Args:
        raiz: La raíz del árbol binario.
        valor: El valor del nodo a buscar.
        
    Returns:
        True si el nodo existe, False en caso contrario.
    """
    if raiz is None:
        return False
        
    if raiz.valor == valor:
        return True
        
    return existe_nodo(raiz.izquierda, valor) or existe_nodo(raiz.derecha, valor)


# Pruebas para la función de ancestro común más cercano
def probar_ancestro_comun_mas_cercano():
    """Prueba la función ancestro_comun_mas_cercano."""
    # Caso de prueba 1: Nodos en diferentes subárboles
    print("\n--- Caso de prueba 1: Nodos en diferentes subárboles ---")
    # Creamos un árbol con esta estructura:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    arbol1 = ArbolBinario()
    arbol1.construir_arbol_desde_lista([1, 2, 3, 4, 5, None, 6])
    
    print("Árbol:")
    arbol1.imprimir_estructura()
    
    # LCA de 4 y 6 debería ser 1
    lca1 = ancestro_comun_mas_cercano(arbol1.raiz, 4, 6)
    print(f"Ancestro común más cercano de 4 y 6: {lca1}")
    
    # Caso de prueba 2: Un nodo es ancestro del otro
    print("\n--- Caso de prueba 2: Un nodo es ancestro del otro ---")
    # Creamos un árbol con esta estructura:
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    arbol2 = ArbolBinario()
    arbol2.construir_arbol_desde_lista([1, 2, 3, 4])
    
    print("Árbol:")
    arbol2.imprimir_estructura()
    
    # LCA de 2 y 4 debería ser 2
    lca2 = ancestro_comun_mas_cercano(arbol2.raiz, 2, 4)
    print(f"Ancestro común más cercano de 2 y 4: {lca2}")
    
    # Caso de prueba 3: Nodos son hermanos
    print("\n--- Caso de prueba 3: Nodos son hermanos ---")
    # Creamos un árbol con esta estructura:
    #      1
    #     / \
    #    2   3
    arbol3 = ArbolBinario()
    arbol3.construir_arbol_desde_lista([1, 2, 3])
    
    print("Árbol:")
    arbol3.imprimir_estructura()
    
    # LCA de 2 y 3 debería ser 1
    lca3 = ancestro_comun_mas_cercano(arbol3.raiz, 2, 3)
    print(f"Ancestro común más cercano de 2 y 3: {lca3}")
    
    # Caso de prueba 4: Un nodo es la raíz
    print("\n--- Caso de prueba 4: Un nodo es la raíz ---")
    # Usamos el mismo árbol del caso 3
    # LCA de 1 y 3 debería ser 1
    lca4 = ancestro_comun_mas_cercano(arbol3.raiz, 1, 3)
    print(f"Ancestro común más cercano de 1 y 3: {lca4}")
    
    # Caso de prueba 5: Nodo no está en el árbol
    print("\n--- Caso de prueba 5: Nodo no está en el árbol ---")
    # Usamos el árbol del caso 1
    # Verificamos primero si los nodos existen
    p, q = 4, 99  # 99 no está en el árbol
    if existe_nodo(arbol1.raiz, p) and existe_nodo(arbol1.raiz, q):
        lca5 = ancestro_comun_mas_cercano(arbol1.raiz, p, q)
        print(f"Ancestro común más cercano de {p} y {q}: {lca5}")
    else:
        print(f"Al menos uno de los nodos ({p}, {q}) no está en el árbol.")
        
# Ejecutar las pruebas
if __name__ == "__main__":
    probar_ancestro_comun_mas_cercano()