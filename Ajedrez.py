from copy import copy, deepcopy

tablero_inicial = [
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


profundidad_maxima = 4

maquina = "n"
mov_final = [-1,-1]
ficha_final = "v"

def movimientoValido(posf):
    return posf[0] >= 0 and posf[0] < 8 and posf[1] >= 0 and posf[1] < 8

def moverFicha(posi,posf,tablero):
    #print ("moverFicha")
    #print (posi,posf)
    ficha = tablero[posi[0]][posi[1]]
    tablero[posi[0]][posi[1]] = "v"
    tablero[posf[0]][posf[1]] = ficha

def muestraTablero(tablero):
    print ("-------------------------")
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            if (len(tablero[i][j]) != 3):
                print (" %r   " % tablero[i][j], end = "")
            else:
                print (" %r " % tablero[i][j], end = "")
        print ("\n")
    print ("-------------------------")

def movTorre(pos,tablero):
    #print ("movTorre")
    tmp = pos[:]
    tmp[1] -= 1
    movimientos = [] #posiciones a las que se puede mover

    tmp = pos[:]
    tmp[1] += 1 # x

    # derecha
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1]  and tablero[tmp[0]][tmp[1]] != "v" ): # si son del mismo color
                movimientos.append(tmp[:])
                break #Si hay dos o mas de otro color seguidos, se come solo al primero
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[1] += 1
        else :
            break

    tmp = pos[:]
    tmp[0] += 1
    # abajo
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si son de diferente color
                movimientos.append(tmp[:])
                break #Si hay dos o mas de otro color seguidos, se come solo al primero
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[0] += 1
        else :
            break

    tmp = pos[:]
    tmp[0] -= 1
    # arriba
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si son del mismo color
                movimientos.append(tmp[:])
                break
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[0]-= 1
        else :
            break

    tmp = pos[:]
    tmp[1] -= 1

    # izquierda
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] ): # si son del mismo color
                movimientos.append(tmp[:])
                break
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[0] -= 1
        else :
            break

    return movimientos

def movCaballo(pos,tablero):
    movimientos = []
    uno = pos[:]
    uno[1] = pos[1]+1
    uno[0] = pos[0]-2
    dos = pos[:]
    dos[1] = pos[1]-1
    dos[0] = pos[0]-2
    tres = pos[:]
    tres[1] = pos[1]+2
    tres[0] = pos[0]-1
    cuatro = pos[:]
    cuatro[1] = pos[1]+2
    cuatro[0] = pos[0]+1
    cinco = pos[:]
    cinco[1] = pos[1]+1
    cinco[0] = pos[0]+2
    seis = pos[:]
    seis[1] = pos[1]-1
    seis[0] = pos[0]+2
    siete = pos[:]
    siete[1] = pos[1]-2
    siete[0] = pos[0]+1
    ocho = pos[:]
    ocho[1] = pos[1]-2
    ocho[0] = pos[0]-1

    posibilidades = [uno,dos,tres,cuatro,cinco,seis,siete,ocho]

    for p in posibilidades:
        if (movimientoValido(p)):
            if (tablero[p[0]][p[1]] == "v"):
                movimientos.append(p)
            if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[p[0]][p[1]] != "v"):
                movimientos.append(p)

    return movimientos

def movAlfil(pos,tablero):
    movimientos = []

    tmp = pos[:]
    tmp[1] = pos[1]-1
    tmp[0] = pos[0]-1

    # arriba izquierda
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si son del mismo color
                movimientos.append(tmp[:])
                break
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[1] -= 1
            tmp[0] -= 1
        else :
            break

    tmp = pos[:]
    tmp[1] = pos[1]+1
    tmp[0] = pos[0]-1

    # arriba derecha
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si son del mismo color
                movimientos.append(tmp[:])
                break
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[1] += 1
            tmp[0] -= 1
        else :
            break

    tmp = pos[:]
    tmp[1] = pos[1]-1
    tmp[0] = pos[0]+1

    # abajo izquierda
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v" ): # si son del mismo color
                movimientos.append(tmp[:])
                break
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[1] -= 1
            tmp[0] += 1
        else :
            break

    tmp = pos[:]
    tmp[1] = pos[1]+1
    tmp[0] = pos[0]+1

    # abajo derecha
    while (True):
        if (movimientoValido(tmp)):
            if (tablero[tmp[0]][tmp[1]] == "v"):
                movimientos.append(tmp[:])
            if (tablero[tmp[0]][tmp[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si son del mismo color
                movimientos.append(tmp[:])
                break
            if (tablero[tmp[0]][tmp[1]][-1] == tablero[pos[0]][pos[1]][-1] and tablero[tmp[0]][tmp[1]] != "v"): # si se encuentra a alguien del mismo color no puede seguir avanzando
                break
            tmp[1] += 1
            tmp[0] += 1
        else :
            break

    return movimientos

def movReina(pos,tablero):
    movimientos1 = movAlfil(pos)
    movimientos2 = movTorre(pos)
    return movimientos1+movimientos2

def movRey(pos,tablero):
    #print ("movRey")
    movimientos = []

    # arriba
    uno = pos[:]
    uno[0] = pos[0]-1

    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno[:])
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[uno[0]][uno[1]] != "v"):
            movimientos.append(uno[:])

    # abajo
    uno = pos[:]
    uno[0] = pos[0]+1
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno[:])
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[uno[0]][uno[1]] != "v"):
            movimientos.append(uno[:])

    # izquierda
    uno = pos[:]
    uno[1] = pos[1]-1
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno[:])
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[uno[0]][uno[1]] != "v"):
            movimientos.append(uno[:])

    # derecha
    uno = pos[:]
    uno[1] = pos[1]+1
    if (movimientoValido(uno)):
        if (tablero[uno[0]][uno[1]] == "v"):
            movimientos.append(uno[:])
        if (tablero[uno[0]][uno[1]][-1] != tablero[pos[0]][pos[1]][-1] and tablero[uno[0]][uno[1]] != "v"):
            movimientos.append(uno[:])

    return movimientos

def movPeon(color,pos,tablero):
    #print ("movPeon")
    movimientos = []
    if (color == "negro"): #hacia abajo

        if (pos[0] == 1): #primera posicion
            uno = pos[:]
            uno[0] = pos[0]+1
            dos = pos[:]
            dos[0] = pos[0]+2

            #diagonales
            tres = pos[:]
            tres[0] = pos[0]+1
            tres[1] = pos[1]+1
            cuatro = pos[:]
            cuatro[0] = pos[0]+1
            cuatro[1] = pos[1]-1

            posibilidades = [uno,dos,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno and p!= dos and tablero[p[0]][p[1]] != "v"):
                        movimientos.append(p)
                        break
                    if (tablero[p[0]][p[1]] == "v" and p!= tres and p!= cuatro):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]] != "v" and p!= tres and p!= cuatro):
                        break


        else :
            uno = pos[:]
            uno[0] = pos[0]+1

            #diagonales
            tres = pos[:]
            tres[0] = pos[0]+1
            tres[1] = pos[1]+1
            cuatro = pos[:]
            cuatro[0] = pos[0]+1
            cuatro[1] = pos[1]-1

            posibilidades = [uno,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v" and p!= tres and p!= cuatro):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno and tablero[p[0]][p[1]] != "v"):
                        movimientos.append(p)
                        break
                    if (tablero[p[0]][p[1]] != "v" and p!= tres and p!= cuatro):
                        break


    if (color == "blanco"): #hacia arriba

        if (pos[0] == 6): #primera posicion
            uno = pos[:]
            uno[0] = pos[0]-1
            dos = pos[:]
            dos[0] = pos[0]-2

            #diagonales
            tres = pos[:]
            tres[0] = pos[0]-1
            tres[1] = pos[1]+1
            cuatro = pos[:]
            cuatro[0] = pos[0]-1
            cuatro[1] = pos[1]-1

            posibilidades = [uno,dos,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v" and p!= tres and p!= cuatro):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno and p!= dos and tablero[p[0]][p[1]] != "v"):
                        movimientos.append(p)
                        break
                    if (tablero[p[0]][p[1]] != "v" and p!= tres and p!= cuatro):
                        break

        else :
            uno = pos[:]
            uno[0] = pos[0]-1

            #diagonales
            tres = pos[:]
            tres[0] = pos[0]-1
            tres[1] = pos[1]+1
            cuatro = pos[:]
            cuatro[0] = pos[0]-1
            cuatro[1] = pos[1]-1

            posibilidades = [uno,tres,cuatro]

            for p in posibilidades:

                if (movimientoValido(p)):
                    if (tablero[p[0]][p[1]] == "v" and p!= tres and p!= cuatro):
                        movimientos.append(p)
                    if (tablero[p[0]][p[1]][-1] != tablero[pos[0]][pos[1]][-1] and p != uno and tablero[p[0]][p[1]] != "v"):
                        movimientos.append(p)
                        break
                    if (tablero[p[0]][p[1]] != "v" and p!= tres and p!= cuatro):
                        break

    return movimientos

def movFicha(ficha,pos,tablero):
    movimientos = []
    if (ficha[1] == "t"):
        movimientos = movTorre(pos,tablero)
    if (ficha[1] == "c"):
        movimientos = movCaballo(pos,tablero)
    if (ficha[1] == "a"):
        movimientos = movAlfil(pos,tablero)
    if (ficha[1:] == "rnn" or ficha[1:] == "rnb"):
        movimientos = movReina(pos,tablero)
    if (ficha[1:] == "rn" or ficha[1:] == "rb"):
        movimientos = movRey(pos,tablero)
    if (ficha[1:] == "pn"):
        movimientos = movPeon("negro",pos,tablero)
    if (ficha[1:] == "pb"):
        movimientos = movPeon("blanco",pos,tablero)

    return movimientos

def BuscarFicha(ficha,tablero):
    for i in range (0,len(tablero)):
        for j in range (0,len(tablero)):
            if (tablero[i][j] == ficha):
                return [i,j]
    return []

#-----------Minimax------------

def juegoTerminado(tablero): # cuando el rey quede en mate
    reyes = []
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            if (tablero[i][j] == "rn" or tablero[i][j] == "rb"):
                reyes.append(tablero[i][j])
            if (len(reyes) == 2):
                return reyes
    return reyes

# http://neverstopbuilding.com/minimax
def analisis(tablero, profundidad, op, reyes):
    if (len(reyes) == 2): 0
    if (reyes[0][-1] == maquina): return 1 - profundidad
    else : return profundidad - 1


def BlueValue(tablero,profundidad):
    print ("BlueValue")
    print ("profundidad : ", profundidad)
    jt = juegoTerminado(tablero)
    if(len(jt) <= 1 or profundidad > profundidad_maxima):
        return analisis(tablero,profundidad,"max",jt)

    maximo = -float('inf')
    mov_final = [-1,-1]
    ficha_final = "v"

    mov_legales = {}

    # crea diccionario con todos los elementos que puede hacer cada ficha
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            if (tablero[i][j] != "v" and tablero[i][j][-1] == "n"):
                ficha = tablero[i][j]
                mov_legales[ficha] = movFicha(ficha,[i,j],tablero)

    for ficha in mov_legales:
        print ("I'm blue", ficha)
        for mov in mov_legales[ficha]:
            if (mov != []):
                #copia = tablero[:]
                copia = deepcopy(tablero)
                posi = BuscarFicha(ficha,copia)
                moverFicha(posi,mov,copia)
                muestraTablero(copia)
                x = RedValue(copia,profundidad+1)
                print ("blue_x : ", x)
                if (x > maximo):
                    maximo = x
                    mov_final = mov
                    ficha_final = ficha

    return [maximo,mov_final,ficha_final]

def RedValue(tablero,profundidad):
    print ("RedValue")
    print ("profundidad : ", profundidad)
    jt = juegoTerminado(tablero)
    if(len(jt) <= 1 or profundidad > profundidad_maxima):
        return analisis(tablero,profundidad,"min",jt)

    minimo = float('inf')

    mov_legales = {}

    # crea diccionario con todos los elementos que puede hacer cada ficha
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            if (tablero[i][j] != "v" and tablero[i][j][-1] == "b"):
                ficha = tablero[i][j]
                mov_legales[ficha] = movFicha(ficha,[i,j],tablero)

    for ficha in mov_legales:
        print ("I'm red", ficha)
        for mov in mov_legales[ficha]:
            if (mov != []):
                copia = deepcopy(tablero)
                posi = BuscarFicha(ficha,copia)
                moverFicha(posi,mov,copia)
                muestraTablero(copia)
                x = BlueValue(copia,profundidad+1)
                print ("red_x : ", x)
                if (type(x) == int):
                    if (x < minimo):
                        minimo = x
                else:
                    if (x[0] < minimo):
                        minimo = x[0]

    return minimo#,mov_final,ficha_final


if __name__ == "__main__":
    #muestraTablero(tablero_inicial)
    #print (movFicha("1pn" , [1,0] , tablero_inicial))
    #moverFicha([0,1],[0,0],tablero_inicial)
    res = BlueValue(tablero_inicial,1)
    print ("resultado : ")
    print ("Debe mover la ficha ", res[2], end = "")
    print (" a la posicion ", res[1])
