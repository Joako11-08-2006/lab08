from collections import deque, defaultdict

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


def recorrido_orden_vertical(raiz):
    """
    Realiza un recorrido en orden vertical de un árbol binario.
    
    Args:
        raiz: La raíz del árbol binario.
        
    Returns:
        Una lista de listas, donde cada lista interior contiene los nodos 
        en el mismo nivel vertical de arriba hacia abajo.
    """
    if not raiz:
        return []
    
    # Usamos un diccionario para agrupar nodos por distancia horizontal
    columnas = defaultdict(list)
    cola = deque([(raiz, 0)])  # (nodo, distancia_horizontal)
    
    min_col = float('inf')
    max_col = float('-inf')
    
    # Hacemos un recorrido BFS (por niveles)
    while cola:
        nodo, col = cola.popleft()
        
        # Actualizamos el rango de columnas
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        
        # Añadimos el nodo a su columna correspondiente
        columnas[col].append(nodo.valor)
        
        # Añadimos los hijos a la cola
        if nodo.izquierda:
            cola.append((nodo.izquierda, col - 1))
        if nodo.derecha:
            cola.append((nodo.derecha, col + 1))
    
    # Construimos el resultado ordenado por columna
    resultado = []
    for col in range(min_col, max_col + 1):
        resultado.append(columnas[col])
    
    return resultado


# Pruebas para la función de recorrido en orden vertical
def probar_recorrido_orden_vertical():
    """Prueba la función recorrido_orden_vertical."""
    # Caso de prueba 1: Árbol binario normal
    print("\n--- Caso de prueba 1: Árbol binario normal ---")
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
    
    resultado1 = recorrido_orden_vertical(arbol1.raiz)
    print(f"Recorrido en orden vertical: {resultado1}")
    # Resultado esperado: [[4], [2], [1, 5], [3], [6]]
    
    # Caso de prueba 2: Árbol vertical en línea
    print("\n--- Caso de prueba 2: Árbol vertical en línea ---")
    # Creamos un árbol con esta estructura:
    #      1
    #     /
    #    2
    #   /
    #  3
    arbol2 = ArbolBinario()
    arbol2.construir_arbol_desde_lista([1, 2, None, 3])
    
    print("Árbol:")
    arbol2.imprimir_estructura()
    
    resultado2 = recorrido_orden_vertical(arbol2.raiz)
    print(f"Recorrido en orden vertical: {resultado2}")
    # Resultado esperado: [[3], [2], [1]]
    
    # Caso de prueba 3: Árbol vacío
    print("\n--- Caso de prueba 3: Árbol vacío ---")
    arbol3 = ArbolBinario()
    
    print("Árbol: (vacío)")
    
    resultado3 = recorrido_orden_vertical(arbol3.raiz)
    print(f"Recorrido en orden vertical: {resultado3}")
    # Resultado esperado: []
    
    # Caso de prueba 4: Árbol con un solo nodo
    print("\n--- Caso de prueba 4: Árbol con un solo nodo ---")
    arbol4 = ArbolBinario()
    arbol4.construir_arbol_desde_lista([1])
    
    print("Árbol:")
    arbol4.imprimir_estructura()
    
    resultado4 = recorrido_orden_vertical(arbol4.raiz)
    print(f"Recorrido en orden vertical: {resultado4}")
    # Resultado esperado: [[1]]
    
    # Caso de prueba 5: Árbol binario completo
    print("\n--- Caso de prueba 5: Árbol binario completo ---")
    # Creamos un árbol con esta estructura:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    arbol5 = ArbolBinario()
    arbol5.construir_arbol_desde_lista([1, 2, 3, 4, 5, 6, 7])
    
    print("Árbol:")
    arbol5.imprimir_estructura()
    
    resultado5 = recorrido_orden_vertical(arbol5.raiz)
    print(f"Recorrido en orden vertical: {resultado5}")
    # Resultado esperado: [[4], [2], [1, 5, 6], [3], [7]]

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_recorrido_orden_vertical()