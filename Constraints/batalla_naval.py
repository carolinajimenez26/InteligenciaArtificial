from constraint import *

if __name__ == "__main__":

    problem = Problem()

    #Numero casillas que deben ser ocupadas en cada fila y cada columna.
    rows_ans = [3,2,3,2]
    cols_ans = [2,4,0,4]

    #Agregar variables
    for i in range(0,len(rows_ans)):
        for j in range(0,len(cols_ans)):
            problem.addVariable(i*len(cols_ans)+j,range(0,2))

    #Restricciones para que las filas sean iguales al numero de casillas que deben ser ocupadas rows_ans[i]
    for i in range(0,len(rows_ans)):
        problem.addConstraint(ExactSumConstraint(rows_ans[i]),[i*len(cols_ans)+col for col in range(0,len(cols_ans))])

    #Restricciones para que las columnas sean iguales al numero de casillas que deben ser ocupadas cols_ans[i]
    for i in range(0,len(cols_ans)):
        problem.addConstraint(ExactSumConstraint(cols_ans[i]),[i+fil*len(rows_ans) for fil in range(0,len(rows_ans))])


    solutions = problem.getSolution()
    if solutions:
        print "Found %d solution(s)!" % len(solutions)

        for i in range(0,len(rows_ans)):
            for j in range(0, len(cols_ans)):
                print solutions[i*len(cols_ans)+j],
            print
    else :
        print "No se encontraron soluciones"
