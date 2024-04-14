import pygame
pygame.init()

"""Este archivo contiene las funciones para el correcto funcionamiento del 
resolutor de sudoku como lo es: dibujar la cuadricula y los botones, resolverlo,
verificar que se puede resolver."""

def tablero_resuelto(tablero):
    """Si hay una casilla vacia la funcion evalua si hay algun numero que 
    encaje en esa casilla. Si el numero encaja en el tablero utiliza la 
    recursividad para rellenar las demas casillas vacias"""
    casilla_vacia = encontrar_casilla_vacia(tablero)
    if not casilla_vacia:
        return True
    
    fila, columna = casilla_vacia
    for num in range(1, 10):
        if posicion_valida(tablero, fila, columna, num):
            tablero[fila][columna] = num
            if tablero_resuelto(tablero):
                return True
            tablero[fila][columna] = 0
    return False


def encontrar_casilla_vacia(tablero):
    """Esta funcion recorre el tablero en busca de una casilla vacia"""
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i,j
    return None


def posicion_valida(tablero, fila, columna, num):
    """Esta funcion verifica si el numero puede ser ingresado en una posicion"""
    #Comprobar si en la misma fila esta ese numero
    for i in range(9):
        if tablero[fila][i] == num:
            return False
    #Comprobar si en la misma columna esta ese numero
    for i in range(9):    
        if tablero[i][columna] == num:
            return False   
    #Comprobar si en esa subcuadricula ya esta ese numero
    fila_inicio, columna_inicio = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if tablero[i][j] == num:
                return False
            
    return True


def comprobar_tablero_U(tablero):
    """Esta funcion verifica si el tablero que ingreso el usuario no tiene 
    numeros en posiciones invalidas. Recorre cada numero del tablero y simula
    que lo va a insertar en esa posicion, esto se hace para reutilzar codigo"""
    for i in range(9):
        for j in range(9):
            if tablero[i][j] != 0:
                numero = tablero[i][j]
                tablero[i][j] = 0
                if posicion_valida(tablero, i, j, numero):
                    tablero[i][j] = numero
                else:
                    tablero[i][j] = numero
                    return False
    return True


def dibujar_tablero(ventana, tablero, tamanio_celda, color_lineas):
    """Esta funcion dibuja el tablero con la ayuda de un bucle anidado,
    generando rectangulos y verifica si en esa misma posicion el tablero tiene
    un numero para escribirlo en ese rectangulo. Ademas cada 3 filas y columnas
    dibuja una linea que separa las subcuadriculas"""
    for fila in range(9):
        for columna in range(9):
            rect_x = columna * tamanio_celda
            rect_y = fila * tamanio_celda
            dimensiones = pygame.Rect(rect_x, rect_y, tamanio_celda, tamanio_celda)
            pygame.draw.rect(ventana, color_lineas, dimensiones, 1)
            if tablero[fila][columna] != 0:
                fuente = pygame.font.Font(None, 75)
                texto = fuente.render(str(tablero[fila][columna]), True, color_lineas)
                texto_rect = texto.get_rect(center= dimensiones.center)
                ventana.blit(texto, texto_rect.topleft)
            if (columna % 3 == 0):
                pygame.draw.line(ventana, color_lineas, (tamanio_celda * columna, 0), (tamanio_celda * columna, 450), 5)
        if (fila % 3 == 0):
            pygame.draw.line(ventana, color_lineas, (0, tamanio_celda * fila), (450, tamanio_celda * fila), 5)
    pygame.draw.line(ventana, color_lineas, (0, 450), (450, 450), 5)


def dibujar_botones(ventana, color_bt, dimen_pos, mensaje, color_txt):
    """Esta funcion permite dibujar botones, como parametros necesita: la
    superfice, el color del boton, la posicion y dimensiones, el texto o 
    mensaje que va a contener y el color de la fuente"""
    pygame.draw.rect(ventana, color_bt, dimen_pos)
    fuente = pygame.font.Font(None, 30)
    texto = fuente.render(mensaje, True, color_txt)
    texto_boton1 = texto.get_rect(center= dimen_pos.center)
    ventana.blit(texto, texto_boton1.topleft)