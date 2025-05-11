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


def podar_arbol(raiz, objetivo):
    """
    Poda un árbol binario eliminando todos los subárboles que no contienen el valor objetivo.
    
    Args:
        raiz: La raíz del árbol binario.
        objetivo: El valor objetivo que debe contener el subárbol para no ser podado.
        
    Returns:
        La nueva raíz del árbol podado, o None si se elimina todo el árbol.
    """
    if raiz is None:
        return None
    
    # Primero procesamos recursivamente los subárboles (post-orden)
    raiz.izquierda = podar_arbol(raiz.izquierda, objetivo)
    raiz.derecha = podar_arbol(raiz.derecha, objetivo)
    
    # Si el nodo actual contiene el valor objetivo, lo mantenemos
    if raiz.valor == objetivo:
        return raiz
    
    # Si alguno de los hijos contiene el valor objetivo, mantenemos este nodo
    if raiz.izquierda is not None or raiz.derecha is not None:
        return raiz
    
    # Si llegamos aquí, ni este nodo ni sus subárboles contienen el valor objetivo
    return None


def contiene_valor(raiz, objetivo):
    """
    Verifica si un árbol contiene el valor objetivo.
    
    Args:
        raiz: La raíz del árbol binario.
        objetivo: El valor a buscar.
        
    Returns:
        True si el árbol contiene el valor, False en caso contrario.
    """
    if raiz is None:
        return False
    
    if raiz.valor == objetivo:
        return True
    
    return contiene_valor(raiz.izquierda, objetivo) or contiene_valor(raiz.derecha, objetivo)


# Pruebas para la función de poda de árboles
def probar_podar_arbol():
    """Prueba la función podar_arbol."""
    # Caso de prueba 1: Árbol binario normal, podar para valor 1
    print("\n--- Caso de prueba 1: Árbol binario normal, podar para valor 1 ---")
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    arbol1 = ArbolBinario()
    arbol1.construir_arbol_desde_lista([1, 2, 3, 4, 5, None, 6])
    
    print("Árbol original:")
    arbol1.imprimir_estructura()
    
    arbol_podado1 = ArbolBinario()
    arbol_podado1.raiz = podar_arbol(arbol1.raiz, 1)
    
    print("Árbol podado (para valor 1):")
    arbol_podado1.imprimir_estructura()
    
    # Caso de prueba 2: Árbol con múltiples ocurrencias del objetivo
    print("\n--- Caso de prueba 2: Árbol con múltiples ocurrencias del objetivo ---")
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  1   5   1
    arbol2 = ArbolBinario()
    arbol2.raiz = NodoArbol(1)
    arbol2.raiz.izquierda = NodoArbol(2)
    arbol2.raiz.derecha = NodoArbol(3)
    arbol2.raiz.izquierda.izquierda = NodoArbol(1)
    arbol2.raiz.izquierda.derecha = NodoArbol(5)
    arbol2.raiz.derecha.derecha = NodoArbol(1)
    
    print("Árbol original:")
    arbol2.imprimir_estructura()
    
    arbol_podado2 = ArbolBinario()
    arbol_podado2.raiz = podar_arbol(arbol2.raiz, 1)
    
    print("Árbol podado (para valor 1):")
    arbol_podado2.imprimir_estructura()
    
    # Caso de prueba 3: Árbol vacío
    print("\n--- Caso de prueba 3: Árbol vacío ---")
    arbol3 = ArbolBinario()
    
    print("Árbol original: (vacío)")
    
    arbol_podado3 = ArbolBinario()
    arbol_podado3.raiz = podar_arbol(arbol3.raiz, 1)
    
    print("Árbol podado (para valor 1): (vacío)")
    
    # Caso de prueba 4: Objetivo no está en el árbol
    print("\n--- Caso de prueba 4: Objetivo no está en el árbol ---")
    #      1
    #     / \
    #    2   3
    arbol4 = ArbolBinario()
    arbol4.construir_arbol_desde_lista([1, 2, 3])
    
    print("Árbol original:")
    arbol4.imprimir_estructura()
    
    arbol_podado4 = ArbolBinario()
    arbol_podado4.raiz = podar_arbol(arbol4.raiz, 4)
    
    print("Árbol podado (para valor 4):")
    if arbol_podado4.raiz is None:
        print("(El árbol quedó vacío después de la poda)")
    else:
        arbol_podado4.imprimir_estructura()
    
    # Caso de prueba 5: Todos los nodos tienen el valor objetivo
    print("\n--- Caso de prueba 5: Todos los nodos tienen el valor objetivo ---")
    #      5
    #     / \
    #    5   5
    arbol5 = ArbolBinario()
    arbol5.raiz = NodoArbol(5)
    arbol5.raiz.izquierda = NodoArbol(5)
    arbol5.raiz.derecha = NodoArbol(5)
    
    print("Árbol original:")
    arbol5.imprimir_estructura()
    
    arbol_podado5 = ArbolBinario()
    arbol_podado5.raiz = podar_arbol(arbol5.raiz, 5)
    
    print("Árbol podado (para valor 5):")
    arbol_podado5.imprimir_estructura()

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_podar_arbol()