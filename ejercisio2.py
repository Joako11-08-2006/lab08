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


def serializar(raiz):
    """
    Serializa un árbol binario a una cadena de texto.
    
    Args:
        raiz: La raíz del árbol binario.
        
    Returns:
        Una cadena de texto que representa el árbol serializado.
    """
    if not raiz:
        return "[]"
    
    resultado = []
    cola = deque([raiz])
    
    while cola:
        nodo = cola.popleft()
        
        if nodo:
            resultado.append(str(nodo.valor))
            cola.append(nodo.izquierda)
            cola.append(nodo.derecha)
        else:
            resultado.append("null")
    
    # Eliminar los "null" al final
    while resultado and resultado[-1] == "null":
        resultado.pop()
    
    return "[" + ",".join(resultado) + "]"


def deserializar(datos):
    """
    Deserializa una cadena de texto para reconstruir un árbol binario.
    
    Args:
        datos: Una cadena de texto que representa el árbol serializado.
        
    Returns:
        La raíz del árbol binario reconstruido.
    """
    # Eliminar los corchetes y dividir por comas
    datos = datos.strip("[]")
    if not datos:
        return None
    
    valores = datos.split(",")
    raiz = NodoArbol(int(valores[0]))
    cola = deque([raiz])
    i = 1
    
    while cola and i < len(valores):
        nodo_actual = cola.popleft()
        
        # Hijo izquierdo
        if i < len(valores):
            if valores[i] != "null":
                nodo_actual.izquierda = NodoArbol(int(valores[i]))
                cola.append(nodo_actual.izquierda)
            i += 1
        
        # Hijo derecho
        if i < len(valores):
            if valores[i] != "null":
                nodo_actual.derecha = NodoArbol(int(valores[i]))
                cola.append(nodo_actual.derecha)
            i += 1
    
    return raiz


def son_arboles_iguales(raiz1, raiz2):
    """
    Comprueba si dos árboles binarios son iguales en estructura y valores.
    
    Args:
        raiz1: La raíz del primer árbol.
        raiz2: La raíz del segundo árbol.
        
    Returns:
        True si los árboles son iguales, False en caso contrario.
    """
    # Si ambos son None, son iguales
    if not raiz1 and not raiz2:
        return True
    
    # Si uno es None y el otro no, son diferentes
    if not raiz1 or not raiz2:
        return False
    
    # Compara los valores y los subárboles recursivamente
    return (raiz1.valor == raiz2.valor and
            son_arboles_iguales(raiz1.izquierda, raiz2.izquierda) and
            son_arboles_iguales(raiz1.derecha, raiz2.derecha))


# Pruebas para las funciones de serialización y deserialización
def probar_serializar_deserializar():
    """Prueba las funciones serializar y deserializar."""
    # Caso de prueba 1: Árbol binario normal
    print("\n--- Caso de prueba 1: Árbol binario normal ---")
    arbol1 = ArbolBinario()
    arbol1.construir_arbol_desde_lista([1, 2, 3, 4, 5, None, 6])
    
    print("Árbol original:")
    arbol1.imprimir_estructura()
    
    serializado1 = serializar(arbol1.raiz)
    print(f"Serializado: {serializado1}")
    
    deserializado1 = deserializar(serializado1)
    arbol_deserializado1 = ArbolBinario()
    arbol_deserializado1.raiz = deserializado1
    
    print("Árbol deserializado:")
    arbol_deserializado1.imprimir_estructura()
    
    print(f"¿Son iguales? {son_arboles_iguales(arbol1.raiz, deserializado1)}")
    
    # Caso de prueba 2: Árbol vacío
    print("\n--- Caso de prueba 2: Árbol vacío ---")
    arbol2 = ArbolBinario()
    
    print("Árbol original: (vacío)")
    
    serializado2 = serializar(arbol2.raiz)
    print(f"Serializado: {serializado2}")
    
    deserializado2 = deserializar(serializado2)
    arbol_deserializado2 = ArbolBinario()
    arbol_deserializado2.raiz = deserializado2
    
    print("Árbol deserializado: (vacío)")
    
    print(f"¿Son iguales? {son_arboles_iguales(arbol2.raiz, deserializado2)}")
    
    # Caso de prueba 3: Árbol con un solo nodo
    print("\n--- Caso de prueba 3: Árbol con un solo nodo ---")
    arbol3 = ArbolBinario()
    arbol3.construir_arbol_desde_lista([42])
    
    print("Árbol original:")
    arbol3.imprimir_estructura()
    
    serializado3 = serializar(arbol3.raiz)
    print(f"Serializado: {serializado3}")
    
    deserializado3 = deserializar(serializado3)
    arbol_deserializado3 = ArbolBinario()
    arbol_deserializado3.raiz = deserializado3
    
    print("Árbol deserializado:")
    arbol_deserializado3.imprimir_estructura()
    
    print(f"¿Son iguales? {son_arboles_iguales(arbol3.raiz, deserializado3)}")
    
    # Caso de prueba 4: Árbol sesgado a la izquierda
    print("\n--- Caso de prueba 4: Árbol sesgado a la izquierda ---")
    arbol4 = ArbolBinario()
    arbol4.construir_arbol_desde_lista([1, 2, None, 3, None, None, None, 4])
    
    print("Árbol original:")
    arbol4.imprimir_estructura()
    
    serializado4 = serializar(arbol4.raiz)
    print(f"Serializado: {serializado4}")
    
    deserializado4 = deserializar(serializado4)
    arbol_deserializado4 = ArbolBinario()
    arbol_deserializado4.raiz = deserializado4
    
    print("Árbol deserializado:")
    arbol_deserializado4.imprimir_estructura()
    
    print(f"¿Son iguales? {son_arboles_iguales(arbol4.raiz, deserializado4)}")
    
    # Caso de prueba 5: Árbol sesgado a la derecha
    print("\n--- Caso de prueba 5: Árbol sesgado a la derecha ---")
    arbol5 = ArbolBinario()
    # Creamos manualmente un árbol sesgado a la derecha para mayor claridad
    arbol5.raiz = NodoArbol(1)
    arbol5.raiz.derecha = NodoArbol(2)
    arbol5.raiz.derecha.derecha = NodoArbol(3)
    arbol5.raiz.derecha.derecha.derecha = NodoArbol(4)
    
    print("Árbol original:")
    arbol5.imprimir_estructura()
    
    serializado5 = serializar(arbol5.raiz)
    print(f"Serializado: {serializado5}")
    
    deserializado5 = deserializar(serializado5)
    arbol_deserializado5 = ArbolBinario()
    arbol_deserializado5.raiz = deserializado5
    
    print("Árbol deserializado:")
    arbol_deserializado5.imprimir_estructura()
    
    print(f"¿Son iguales? {son_arboles_iguales(arbol5.raiz, deserializado5)}")

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_serializar_deserializar()