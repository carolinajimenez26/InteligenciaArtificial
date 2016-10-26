#Usando CSP desde AIMA Python
#Metodo MapColoringCSP , se definen el problema de los 4 colores similar al planteado de colombia (Para australia solo necesito 3)

australia = MapColoringCSP(list('RGB'), 'SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T:')

SA: Souther Australia
WA: Western Australia
NT: NorthWest Territories
Q: Queensland
NSQ: New South Waller
V: Victoria
T: Tasmania

#Nota: Revisar class CSP(search.Problem) /def AC3 (csp, quene=None, removals=None) / def BackTracking_search(csp,...)
