tablero = [
    ["1tn","1cn","1an","rnn","rn","2an","2cn","2tn"],
    ["1pn","2pn","3pn","4pn","5pn","6pn","7pn","8pn"],
    ["v","v","v","v","v","v","v","v"],
    ["v","v","v","v","v","v","v","v"],
    ["v","v","v","v","v","v","v","v"],
    ["v","v","v","v","v","v","v","v"],
    ["1pb","2pb","3pb","4pb","5pb","6pb","7pb","8pb"],
    ["1tb","1cb","1ab","rnb","rb","2ab","2cb","2tb"]
]

jerarquia = ["peon", "caballo", "alfil", "torre", "reina", "rey"]

profundidad_maxima = 10

def movimientoValido(posf):
    return posf[0] >= 0 and posf[0] < 8 and posf[1] >= 0 and posf[1] < 8

def moverFicha(posi,posf,tablero_aux):
    print (posi,posf)
    ficha = tablero_aux[posi[0]][posi[1]]
    tablero_aux[posi[0]][posi[1]] = "v"
    tablero_aux[posf[0]][posf[1]] = ficha

def movTorre(pos):
    print ("movTorre")
    tmp = pos
    tmp[1] -= 1
    movimientos = [] #posiciones a las que se puede mover
    # arriba
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[pos[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[pos[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[1] -= 1
        else :
            break

    tmp = pos
    tmp[1] += 1

    # abajo
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[1] += 1
        else :
            break

    tmp = pos
    tmp[0] -= 1

    # izquierda
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[0] -= 1
        else :
            break

    tmp = pos
    tmp[0] += 1

    # derecha
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[0] += 1
        else :
            break

    return movimientos


def movCaballo(pos):
    print ("movCaballo")
    movimientos = []
    uno = pos
    uno[0] = pos[0]+1
    uno[1] = pos[1]-2
    dos = pos
    dos[0] = pos[0]-1
    dos[1] = pos[1]-2
    tres = pos
    tres[0] = pos[0]+2
    tres[1] = pos[1]-1
    cuatro = pos
    cuatro[0] = pos[0]+2
    cuatro[1] = pos[1]+1
    cinco = pos
    cinco[0] = pos[0]+1
    cinco[1] = pos[1]+2
    seis = pos
    seis[0] = pos[0]-1
    seis[1] = pos[1]+2
    siete = pos
    siete[0] = pos[0]-2
    siete[1] = pos[1]+1
    ocho = pos
    ocho[0] = pos[0]-2
    ocho[1] = pos[1]-1

    posibilidades = [uno,dos,tres,cuatro,cinco,seis,siete,ocho]

    for p in posibilidades:
        if (movimientoValido(p)):
            if (tablero[p[0]][p[1]] == "v"):
                movimientos.append(p)
            if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1]):
                movimientos.append(p)

    return movimientos

def movAlfil(pos):
    print ("movAlfil")
    movimientos = []

    tmp = pos
    tmp[0] = pos[0]-1
    tmp[1] = pos[1]-1

    # arriba izquierda
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[0] -= 1
            tmp[1] -= 1
        else :
            break

    tmp[0] = pos[0]+1
    tmp[1] = pos[1]-1

    # arriba derecha
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[0] += 1
            tmp[1] -= 1
        else :
            break

    tmp[0] = pos[0]-1
    tmp[1] = pos[1]+1

    # abajo izquierda
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[0] -= 1
            tmp[1] += 1
        else :
            break

    tmp[0] = pos[0]+1
    tmp[1] = pos[1]+1

    # abajo derecha
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp)
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp)
                break
            tmp[0] += 1
            tmp[1] += 1
        else :
            break

    return movimientos

def movReina(pos):
    print ("movReina")
    movimientos1 = movAlfil(pos)
    movimientos2 = movTorre(pos)
    return movimientos1+movimientos2

def movRey(pos):
    print ("movRey")
    movimientos = []
    # arriba
    uno = pos
    uno[0] = pos[0]
    uno[1] = pos[1]-1
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno)
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1]):
            movimientos.append(uno)
    # abajo
    uno[1] = pos[1]+1
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno)
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1]):
            movimientos.append(uno)
    # izquierda
    uno[0] = pos[0]-1
    uno[1] = pos[1]
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno)
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1]):
            movimientos.append(uno)
    # derecha
    uno[0] = pos[0]+1
    uno[1] = pos[1]
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno)
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1]):
            movimientos.append(uno)

    return movimientos

def movPeon(pos,color):
    print ("movPeon")
    movimientos = []
    if (color == "negro"): #hacia abajo

        if (pos[1] == 1): #primera posicion
            uno = pos
            uno[1] = pos[1]+1
            dos = pos
            dos[1] = pos[1]+2

            #diagonales
            tres[1] = pos[1]+1
            tres[0] = pos[0]+1
            cuatro[1] = pos[1]+1
            cuatro[0] = pos[0]-1

            posibilidades = [uno,dos,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v"):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno and p!= dos):
                        movimientos.append(p)

        else :
            uno = pos
            uno[1] = pos[1]+1

            #diagonales
            tres[1] = pos[1]+1
            tres[0] = pos[0]+1
            cuatro[1] = pos[1]+1
            cuatro[0] = pos[0]-1

            posibilidades = [uno,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v"):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno):
                        movimientos.append(p)


    if (color == "blanco"): #hacia arriba

        if (pos[1] == 6): #primera posicion
            uno = pos
            uno[1] = pos[1]-1
            dos = pos
            dos[1] = pos[1]-2

            #diagonales
            tres[1] = pos[1]-1
            tres[0] = pos[0]+1
            cuatro[1] = pos[1]-1
            cuatro[0] = pos[0]-1

            posibilidades = [uno,dos,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v"):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno and p!= dos):
                        movimientos.append(p)

        else :
            uno = pos
            uno[1] = pos[1]-1

            #diagonales
            tres[1] = pos[1]-1
            tres[0] = pos[0]+1
            cuatro[1] = pos[1]-1
            cuatro[0] = pos[0]-1

            posibilidades = [uno,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v"):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno):
                        movimientos.append(p)

    return movimientos

def movFicha(ficha,pos):
    movimientos = []
    if (ficha[1] == "t"):
        movimientos = movTorre(pos)
    if (ficha[1] == "c"):
        movimientos = movCaballo(pos)
    if (ficha[1] == "a"):
        movimientos = movAlfil(pos)
    if (ficha[1:] == "rnn" or ficha[1:] == "rnb"):
        movimientos = movReina(pos)
    if (ficha[1:] == "rn" or ficha[1:] == "rb"):
        movimientos = movRey(pos)
    if (ficha[1:] == "pn"):
        movimientos = movPeon("negro",pos)
    if (ficha[1:] == "pb"):
        movimientos = movPeon("blanco",pos)

    return movimientos,pos

def BuscarFicha(ficha,tablero_aux):
    for i in range (0,len(tablero_aux)):
        for j in range (0,len(tablero_aux)):
            if (tablero_aux[i][j]):
                return [i,j]

#-----------Minimax------------

def juegoTerminado(tablero_aux):
    pass

def BlueValue(tablero_aux,profundidad):
    if(juegoTerminado(tablero_aux) or profundidad > profundidad_maxima):
        return analisis(tablero_aux)

    maximo = -float('inf')
    mov_final = [-1,-1]
    ficha_final = "v"

    mov_legales = {}

    # crea diccionario con todos los elementos que puede hacer cada ficha
    for i in range(0,len(tablero_aux)):
        for j in range(0,len(tablero_aux)):
            if (tablero_aux[i][j] != "v"):
                ficha = tablero_aux[i][j]
                mov_legales[ficha] = movFicha(ficha,[i,j])

    for ficha in mov_legales:
        for mov in mov_legales[ficha]:
            if (mov != []):
                copia = tablero_aux[:]
                posi = BuscarFicha(ficha,copia)
                print ("posi : ",posi)
                print ("mov: ", mov)
                moverFicha(posi,mov,copia)
                x = RedValue(copia,profundidad+1)
                if (x > maximo):
                    maximo = x
                    mov_final = mov
                    ficha_final = ficha

    return maximo

def RedValue(tablero_aux,profundidad):
    if(juegoTerminado(tablero_aux) or profundidad > profundidad_maxima):
        return analisis(tablero_aux)

    minimo = float('inf')
    mov_final = [-1,-1]
    ficha_final = "v"

    mov_legales = {}

    # crea diccionario con todos los elementos que puede hacer cada ficha
    for i in range(0,len(tablero_aux)):
        for j in range(0,len(tablero_aux)):
            if (tablero_aux[i][j] != "v"):
                ficha = tablero_aux[i][j]
                mov_legales[ficha] = movFicha(ficha,[i,j])
                print ("movimientos en ficha : ", ficha)
                print (mov_legales[ficha])

    for ficha in mov_legales:
            for mov in mov_legales[ficha]:
                copia = tablero_aux[:]
                posi = BuscarFicha(ficha,copia)
                moverFicha(posi,mov,copia)
                x = BlueValue(copia,profundidad+1)
                if (x < minimo):
                    minimo = x
                    mov_final = mov
                    ficha_final = ficha

    return minimo


if __name__ == "__main__":
    BlueValue(tablero,1)
