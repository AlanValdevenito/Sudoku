import sudoku
import random
import mapas

def imprimir_numeros_sudoku(sudo, i):
    """
    Funcion que dado un sudoku y un indice que corresponde a la fila, nos imprime en pantalla los valores del
    sudoku con una separacion entre regiones.
    """

    for j in range(len(sudo)):
        if j in valores_a_separar(sudo):
            print(sudo[i][j], "║" , end = " ")
        else:
            print(sudo[i][j], end = " ")

def valores_a_separar(sudo):
    """
    Funcion que dado un sudoku, nos devuelve los valores en donde hay que separar las regiones. 
    """
    
    regiones_a_separar = []
    for i in range(2, len(sudo), 3):
        regiones_a_separar.append(i)

    return regiones_a_separar

def imprimir_sudoku_visual(sudo):
    """
    Funcion que dado un sudoku, nos lo devuelve con una ayuda visual.
    """

    for j in range(len(sudo)):
        if j == 0:
            print("    ", end = "")
        print(j , end = " ")
        if j in valores_a_separar(sudo):
            print(" ", end = " ")
  
    print()   

    for i in range(len(sudo)):
        if i == 0:
            print("   " + "══" * len(sudo) + "═" * (len(sudo)//2))
        print(i , "║ " , end = "")
        imprimir_numeros_sudoku(sudo, i)
        print()
        if i in valores_a_separar(sudo):
            print("   " + "══" * len(sudo) + "═" * (len(sudo)//2))          

    print()

def datos_no_correctos_interfaz(opcion):
    """
    Funcion que revisa los datos ingresados por el usuario en la interfaz.
    Nos devuelve False si lo ingresado es correcto, y nos devuelve True si lo ingresado es incorrecto.
    """

    if opcion == "A" or opcion == "B" or opcion == "S":
        return False
    
    return True

def reingresar_datos_interfaz(opcion):
    """
    Funcion que dada una opcion revisa si la misma es correcta y en caso de no serlo le vueelve a pedir al
    usuario introducir una opcion valida. Devuelve la opcion valida.
    """

    while datos_no_correctos_interfaz(opcion) == True:
        print()
        print("Ingrese una opcion valida.")
        opcion = str(input("Introduzca la opcion deseada: "))

    return opcion
    
def datos_no_correctos_B(parametros2):
    """
    Funcion que revisa los datos ingresados por el usuario en la opcion B.
    Nos devuelve False si lo ingresado es correcto, y nos devuelve True si lo ingresado es incorrecto.
    """

    for i in range(0,9):
        for j in range(0,9):
            if parametros2 == [str(i),str(j)]:
                return False
            
    return True

def datos_no_correctos_A(parametros2):
    """
    Funcion que revisa los datos ingresados por el usuario en la opcion A.
    Nos devuelve False si lo ingresado es correcto, y nos devuelve True si lo ingresado es incorrecto.
    """

    for i in range(0,10):
        for j in range(0,10):
            for x in range(0,10):
                if parametros2 == [str(i),str(j),str(x)]:
                    return False     
    
    return True

def volver_atras(parametros, sudo):
    """
    Funcion que recibe el parametro "atras" y revisa que la opcion ingresada por el usuario para elegir otra opcion
    sea correcta. Nos devuelve la opcion elegida por el usuario.
    """
    
    opcion = str(input("Introduzca la opcion deseada: "))
        
    while datos_no_correctos_interfaz(opcion) == True:
        print()
        print("Ingrese una opcion valida.")
        opcion = str(input("Introduzca la opcion deseada: "))

    return opcion, sudo

def sudoku_borrar(sudo, fila, columna):
    """
    Funcion que dado el sudoku, fila y columna borra el valor en la celda ingresada por el usuario. Devuelve el sudoku
    sin el valor que estaba en la celda.
    """
    
    sudoku_nuevo = sudoku.borrar_valor(sudo, fila, columna)
    imprimir_sudoku_visual(sudoku_nuevo)
    sudo = sudoku_nuevo

    return sudo
    
def sudoku_insertar(sudo, fila, columna, valor):
    """
    Funcion que dado el sudoku, fila, columna y valor inserta el valor en la celda ingresada por el usuario. Devuelve
    el sudoku con el valor nuevo en la celda ingresada.
    """

    sudoku_nuevo = sudoku.insertar_valor(sudo, fila, columna, valor)
    imprimir_sudoku_visual(sudoku_nuevo)
    sudo = sudoku_nuevo

    return sudo

def opcion_A(opcion, sudo):

    parametros = input("Introduce un valor a añadir [fila, columna, valor | atras]: ") 
    parametros2 = parametros.split(",")

    while datos_no_correctos_A(parametros2) == True:
        if parametros == "atras":
            print()
            opcion, sudo = volver_atras(parametros, sudo)
            return opcion, sudo
                        
        else:
            print()
            print("Ingrese una opcion valida.")
            parametros = input("Introduce un valor a añadir [fila, columna, valor | atras ]: ")
            parametros2 = parametros.split(",")
            
    fila = int(parametros2[0])
    columna = int(parametros2[1])
    valor = int(parametros2[2])
    print()
    sudo = sudoku_insertar(sudo, fila, columna, valor)

    if sudoku.hay_movimientos_posibles(sudo):
        print("¡Aun queda al menos un movimiento posible!.")
        return opcion, sudo
    else:
        print("¡Felicitaciones, completaste el Sudoku!.")
        opcion = "S"
        return opcion, sudo

def opcion_B(opcion, sudo):

    parametros = input("Introduce una posicion a borrar [fila, columna | atras]: ")
    parametros2 = parametros.split(",")
            
    while datos_no_correctos_B(parametros2) == True:
        if parametros == "atras":
            print()
            opcion, sudo = volver_atras(parametros, sudo)
            return opcion, sudo
                 
        else: 
            print()
            print("Ingrese una opcion valida.")
            parametros = input("Introduce una posicion a borrar [fila, columna| atras ]: ")
            parametros2 = parametros.split(",")
 
    fila = int(parametros2[0])
    columna = int(parametros2[1])
    print()
    sudo = sudoku_borrar(sudo, fila, columna)
    return opcion, sudo

def main():
    """
    Interfaz del juego. Nos muestra el Sudoku en juego, nos indica que opciones tenemos y nos pide ingresar una opcion.
    """
    
    print("¡Bienvenido/a!")
    print("══════════════")
    sudo = sudoku.crear_juego(random.choice(mapas.MAPAS))
    imprimir_sudoku_visual(sudo)
    
    print("""Instrucciones
═════════════

A: Añadir un numero a una celda.
B: Borrar un numero de una celda.
S: Salir del juego.""")

    print()
    opcion = str(input("Introduzca la opcion deseada: "))
    opcion = reingresar_datos_interfaz(opcion)

    while opcion == "A" or opcion == "B" or opcion == "S":

        if opcion == "A":
            opcion, sudo = opcion_A(opcion, sudo)
                    
        if opcion == "B":
            opcion, sudo = opcion_B(opcion, sudo) 

        if opcion == "S":
            return
    
main()
