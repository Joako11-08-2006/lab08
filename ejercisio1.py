class Nodo:
    """Clase para representar un nodo en el árbol binario de búsqueda."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    """Clase para representar un árbol binario de búsqueda."""
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        """Función auxiliar recursiva para insertar un valor."""
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def recorrido_inorden(self):
        """Realiza un recorrido inorden del árbol y devuelve una lista de valores."""
        resultado = []
        self._recorrido_inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _recorrido_inorden_recursivo(self, nodo, resultado):
        """Función auxiliar recursiva para el recorrido inorden."""
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._recorrido_inorden_recursivo(nodo.derecha, resultado)
    
    def altura(self):
        """Calcula la altura del árbol."""
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        """Función auxiliar recursiva para calcular la altura."""
        if nodo is None:
            return 0
        
        altura_izquierda = self._altura_recursiva(nodo.izquierda)
        altura_derecha = self._altura_recursiva(nodo.derecha)
        
        return max(altura_izquierda, altura_derecha) + 1
    
    def esta_balanceado(self):
        """Verifica si el árbol está balanceado."""
        return self._esta_balanceado_recursivo(self.raiz)
    
    def _esta_balanceado_recursivo(self, nodo):
        """Función auxiliar recursiva para verificar si el árbol está balanceado."""
        if nodo is None:
            return True
        
        altura_izquierda = self._altura_recursiva(nodo.izquierda)
        altura_derecha = self._altura_recursiva(nodo.derecha)
        
        # Un árbol está balanceado si la diferencia de altura entre los subárboles
        # izquierdo y derecho no es mayor que 1, y ambos subárboles están balanceados
        if abs(altura_izquierda - altura_derecha) <= 1 and \
           self._esta_balanceado_recursivo(nodo.izquierda) and \
           self._esta_balanceado_recursivo(nodo.derecha):
            return True
        
        return False
    
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


def balancear_arbol(arbol):
    """
    Convierte un árbol binario de búsqueda en un árbol balanceado.
    
    Args:
        arbol: Un objeto ArbolBinarioBusqueda potencialmente no balanceado.
        
    Returns:
        Un nuevo ArbolBinarioBusqueda balanceado con los mismos nodos.
    """
    # Paso 1: Realizar un recorrido inorden para obtener un array ordenado de valores
    valores_ordenados = arbol.recorrido_inorden()
    
    # Paso 2: Construir un BST balanceado a partir del array ordenado
    arbol_balanceado = ArbolBinarioBusqueda()
    arbol_balanceado.raiz = _construir_arbol_balanceado(valores_ordenados, 0, len(valores_ordenados) - 1)
    
    return arbol_balanceado

def _construir_arbol_balanceado(valores, inicio, fin):
    """
    Función auxiliar recursiva para construir un árbol balanceado.
    Utiliza una estrategia de divide y vencerás.
    
    Args:
        valores: Lista ordenada de valores.
        inicio: Índice de inicio.
        fin: Índice de fin.
        
    Returns:
        La raíz del árbol balanceado.
    """
    # Caso base
    if inicio > fin:
        return None
    
    # Encuentra el elemento medio y lo usa como raíz
    medio = (inicio + fin) // 2
    nodo = Nodo(valores[medio])
    
    # Construye recursivamente los subárboles izquierdo y derecho
    nodo.izquierda = _construir_arbol_balanceado(valores, inicio, medio - 1)
    nodo.derecha = _construir_arbol_balanceado(valores, medio + 1, fin)
    
    return nodo


# Pruebas para la función de balanceo de árbol
def probar_balanceo_arbol():
    """Prueba la función balancear_arbol."""
    # Caso de prueba 1: Árbol ya balanceado
    print("\n--- Caso de prueba 1: Árbol ya balanceado ---")
    arbol1 = ArbolBinarioBusqueda()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        arbol1.insertar(val)
    
    print("Árbol original:")
    arbol1.imprimir_estructura()
    print(f"¿Está balanceado? {arbol1.esta_balanceado()}")
    
    balanceado1 = balancear_arbol(arbol1)
    print("\nÁrbol balanceado:")
    balanceado1.imprimir_estructura()
    print(f"¿Está balanceado? {balanceado1.esta_balanceado()}")
    print(f"Recorrido inorden original: {arbol1.recorrido_inorden()}")
    print(f"Recorrido inorden balanceado: {balanceado1.recorrido_inorden()}")
    
    # Caso de prueba 2: Árbol sesgado a la derecha
    print("\n--- Caso de prueba 2: Árbol sesgado a la derecha ---")
    arbol2 = ArbolBinarioBusqueda()
    for val in [1, 2, 3, 4, 5]:
        arbol2.insertar(val)
    
    print("Árbol original:")
    arbol2.imprimir_estructura()
    print(f"¿Está balanceado? {arbol2.esta_balanceado()}")
    
    balanceado2 = balancear_arbol(arbol2)
    print("\nÁrbol balanceado:")
    balanceado2.imprimir_estructura()
    print(f"¿Está balanceado? {balanceado2.esta_balanceado()}")
    print(f"Recorrido inorden original: {arbol2.recorrido_inorden()}")
    print(f"Recorrido inorden balanceado: {balanceado2.recorrido_inorden()}")
    
    # Caso de prueba 3: Árbol sesgado a la izquierda
    print("\n--- Caso de prueba 3: Árbol sesgado a la izquierda ---")
    arbol3 = ArbolBinarioBusqueda()
    for val in [5, 4, 3, 2, 1]:
        arbol3.insertar(val)
    
    print("Árbol original:")
    arbol3.imprimir_estructura()
    print(f"¿Está balanceado? {arbol3.esta_balanceado()}")
    
    balanceado3 = balancear_arbol(arbol3)
    print("\nÁrbol balanceado:")
    balanceado3.imprimir_estructura()
    print(f"¿Está balanceado? {balanceado3.esta_balanceado()}")
    print(f"Recorrido inorden original: {arbol3.recorrido_inorden()}")
    print(f"Recorrido inorden balanceado: {balanceado3.recorrido_inorden()}")
    
    # Caso de prueba 4: Árbol vacío
    print("\n--- Caso de prueba 4: Árbol vacío ---")
    arbol4 = ArbolBinarioBusqueda()
    
    print("Árbol original: (vacío)")
    print(f"¿Está balanceado? {arbol4.esta_balanceado()}")
    
    balanceado4 = balancear_arbol(arbol4)
    print("\nÁrbol balanceado: (vacío)")
    print(f"¿Está balanceado? {balanceado4.esta_balanceado()}")
    print(f"Recorrido inorden original: {arbol4.recorrido_inorden()}")
    print(f"Recorrido inorden balanceado: {balanceado4.recorrido_inorden()}")
    
    # Caso de prueba 5: Árbol con un solo nodo
    print("\n--- Caso de prueba 5: Árbol con un solo nodo ---")
    arbol5 = ArbolBinarioBusqueda()
    arbol5.insertar(42)
    
    print("Árbol original:")
    arbol5.imprimir_estructura()
    print(f"¿Está balanceado? {arbol5.esta_balanceado()}")
    
    balanceado5 = balancear_arbol(arbol5)
    print("\nÁrbol balanceado:")
    balanceado5.imprimir_estructura()
    print(f"¿Está balanceado? {balanceado5.esta_balanceado()}")
    print(f"Recorrido inorden original: {arbol5.recorrido_inorden()}")
    print(f"Recorrido inorden balanceado: {balanceado5.recorrido_inorden()}")

# Ejecutar las pruebas
if __name__ == "__main__":
    probar_balanceo_arbol()