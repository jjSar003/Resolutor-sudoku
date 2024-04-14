import pygame
pygame.init()

import funciones_sudoku as fns

def resolver_sudoku():
    """Esta funcion comprueba si es posible resolver el sudoku y luego llama a 
    la funcion que resuelve el sudoku. Ademas esta funcion asigna el color 
    del mensaje de error, para que solo se muestre si es necesario."""
    verificacion = fns.comprobar_tablero_U(tablero)      
    if verificacion:
        fns.tablero_resuelto(tablero)
        color_error = blanco
    else:
        color_error = negro  
    
    return color_error
    

#Configuración de la ventana
ancho_ventana, altura_ventana = 450, 535
ventana = pygame.display.set_mode((ancho_ventana, altura_ventana))
pygame.display.set_caption("Sudoku")

#Tamaño de la cuadrícula
tamanio_cuadricula = 9
tamanio_celda = ancho_ventana // tamanio_cuadricula

#Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0,255,0)
naranja = (255, 165, 0)

#Colores predeterminados de los botones y el mensaje de error
color_bt_resolver = blanco
color_bt_restablecer = blanco
color_error = blanco

#Matriz que almacenara los numeros del sudoku
tablero = [[0] * 9 for _ in range(9)]

#Posicion y dimensiones de los botones
bt_restablecer = pygame.Rect(60, 460, 135, 30)
bt_resolver = pygame.Rect(255, 460, 135, 30)

# Bucle principal
ejecucion = True
while ejecucion:
    #Asignar el blanco a la ventana
    ventana.fill(blanco)
    #Verificar el cierre del programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecucion = False

        #Verificar el usuario pulsa algun boton del mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Si se presiono un boton o se mostro el mensaje de error y luego 
            #hay un click se restablece el color original
            color_bt_resolver = blanco
            color_bt_restablecer = blanco 
            color_error = blanco
            #Verificar si se hace click en el boton resolver
            if bt_resolver.collidepoint(event.pos):
                #El boton cambia de color y se llama a la funcion que resuelve 
                #el sudoku
                color_bt_resolver = verde
                color_error = resolver_sudoku()     

            #Verifica si se hace click en el boton restablecer
            elif bt_restablecer.collidepoint(event.pos):
                #Se cambia el color y se restablece el sudoku llenandolo de 
                #ceros
                color_bt_restablecer = naranja
                tablero = [[0] * 9 for _ in range(9)]
        
            #Verifica si se usa el boton izquierdo del mouse
            elif event.button == 1:
                #Toma las coordenadas de la posicion del mouse
                #Si fue encima del tablero se guarda la fila y la columna
                x,y = event.pos
                if x <= 450 and y <= 450:
                    fila = y // tamanio_celda
                    columna = x // tamanio_celda
                #De lo contrario se inicializan con -1 para evitar errores en
                #el programa
                else:
                    fila, columna = -1, -1

        #Verificar si se oprime una tecla
        elif event.type == pygame.KEYDOWN:
            #Si la tecla es numerica se almacena para ser puesta en el tablero
            if event.unicode.isdigit():
                numero = int(event.unicode)
                #Verificar si fila y columna no estan vacias
                if fila >= 0 and columna >= 0:
                    if tablero[fila][columna] == 0:
                        tablero[fila][columna] = numero

                    #Si la posicion esta ocupada se remplaza momentaneamente 
                    #por cero para que la celda cambie a blanco y luego se
                    #almacena el numero
                    else:
                        tablero[fila][columna] = 0
                        tablero[fila][columna] = numero

        #Cambia los valores de fila y columna despues de que la tecla fue                
        #oprimida para evitar remplazos involuntarios
        elif event.type == pygame.KEYUP:
            fila, columna = -1, -1

    #Llamado a la funcion que dibuja el tablero
    fns.dibujar_tablero(ventana, tablero, tamanio_celda, negro)

    #Llamado a la funcion que dibuja los botones
    mensaje = "Restablecer"
    fns.dibujar_botones(ventana, negro, bt_restablecer, mensaje, color_bt_restablecer)
    mensaje = "Resolver"
    fns.dibujar_botones(ventana, negro, bt_resolver, mensaje, color_bt_resolver)

    #Creacion del mensaje de error 
    fuente = pygame.font.Font(None, 25)
    mensaje = "El sudoku tiene numeros en posiciones invalidas"
    texto = fuente.render(mensaje, True, color_error)
    ventana.blit(texto, (450 // 2 - texto.get_width() // 2, 500))

    pygame.display.flip()
pygame.quit()