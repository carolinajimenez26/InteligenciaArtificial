
def ValidaMovimiento(ficha):
    flag = ficha.x >= 0 and ficha.x < 8 and ficha.y >= 0 and ficha.y < 8
    return flag

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Ajedrez():
    def __init__(self):
        self.tablero = []
        for i in range(0,8):
            ans = []
            for j in range(0,8):
                p = Point(i,j)
                v = Vacio("",p,"",self)
                ans.append(v)
            self.tablero = ans

    def sobreEscribir(self,tablero):
        self.tablero = tablero

    def mueveFicha(self,ficha,p2):
        v = Vacio()
        self.tablero[ficha.pos.x][ficha.pos.y] = v
        self.tablero[p2.x][p2.y] = ficha

    def agregaFicha(self,ficha):
        print (ficha.s)
        print ()
        self.tablero[ficha.pos.x][ficha.pos.y] = ficha
        print ("wi")

    def muestra(self):
        for i in range (0, len(self.tablero)):
            for j in range (0, len(self.tablero)):
                print (self.tablero[i][j])
                print (self.tablero[i][j].muestra()),
            print

class Ficha():
    def __init__(self,color,pos,s,tablero):
        self.color = color
        self.pos = pos
        self.primero = False
        self.s = s
        self.tablero = tablero

    def __repr__(self):
        return "%r" % self.s

class Vacio(Ficha):
    pass

class Peon(Ficha):

    def __init__(self):
        self.primero = False

    def PosiblesMovimientos(self):
        res = []
        if (self.color == "blaco"):
            if (primero) :
                if (ValidaMovimiento(self.pos.x,self.pos.y-2)):
                    p = Point(self.pos.x,self.pos.y-2)
                    res.append(p)

        if (self.color == "negro"):
            pass

class Torre(Ficha):
    pass

class Caballo(Ficha):
    pass

class Alfil(Ficha):
    pass

class Reina(Ficha):
    pass

class Rey(Ficha):
    pass

def init(tablero,ajedrez):
    p = Point()
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            print (p.x,p.y)
            if (tablero[i][j] == "tn"):
                p.x,p.y = i,j
                ficha = Torre("negro",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "cn"):
                p.x,p.y = i,j
                ficha = Caballo("negro",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "an"):
                p.x,p.y = i,j
                ficha = Alfil("negro",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "rnn"):
                p.x,p.y = i,j
                ficha = Reina("negro",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "rn"):
                p.x,p.y = i,j
                ficha = Rey("negro",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "pn"):
                p.x,p.y = i,j
                ficha = Peon("negro",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "tb"):
                p.x,p.y = i,j
                ficha = Torre("blaco",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "cb"):
                p.x,p.y = i,j
                ficha = Caballo("blaco",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "ab"):
                p.x,p.y = i,j
                ficha = Alfil("blaco",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "rnb"):
                p.x,p.y = i,j
                ficha = Reina("blaco",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "rb"):
                p.x,p.y = i,j
                ficha = Rey("blaco",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "pb"):
                p.x,p.y = i,j
                ficha = Peon("blaco",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(ficha)
            if (tablero[i][j] == "v"):
                p.x,p.y = i,j
                v = Vacio("",p,tablero[i][j],ajedrez)
                ajedrez.agregaFicha(v)


if __name__ == "__main__":
    tablero = Ajedrez()
    tablero.muestra()
    tablero_tmp = [
        ["tn","cn","an","rnn","rn","an","cn","tn"],
        ["pn","pn","pn","pn","pn","pn","pn","pn"],
        ["v","v","v","v","v","v","v","v"],
        ["v","v","v","v","v","v","v","v"],
        ["v","v","v","v","v","v","v","v"],
        ["v","v","v","v","v","v","v","v"],
        ["pb","pb","pb","pb","pb","pb","pb","pb"],
        ["tb","cb","ab","rnb","rb","ab","cb","tb"]
    ]

    #init(tablero_tmp,tablero)
    #tablero.muestra()
