def encontrar_el_1000():
# listaA es el conjunto de posibles números A de las disintas
# tripletas pitagoricas
    listaA = list()
# listaA es el conjunto de posibles números B de las disintas
# tripletas pitagoricas
    listaB = list()
# listaA es el conjunto de posibles números c de las disintas
# tripletas pitagoricas
    listaC = list()
#Es la suma de los distintos A + B + C que se generaron haciendo las 
# tripletas
    lista_final = list()
#Se inicializa para indicar las posiciones en las listas
    num = 0
#For para que genera los diferentes números p de la ecuación
    for p in range(30):
#For para que genera los diferentes números 1 de la ecuación
        for q in range(30):
            # En la ecuación p siempre tiene que mas mayor a q
            if p < q:
            # En los caso que p fuera 0 se escribirian datos sin uso futuro.
                if p > 0:
                    if q > 0:         
                        # Ecuación para hallar el número A de la ecuación            
                        listaA.append(p**2 + q**2)
                        # Ecuación para hallar el número A de la ecuación
                        listaB.append(2*p*q)
                        # Ecuación para hallar el número A de la ecuación
                        listaC.append(q**2 - p**2)
                        # Ecuación para sumar los diferentes A, B y C
                        lista_final.append(listaA[num] + listaB[num] + listaC[num])
                        if lista_final[num] == 1000:
                            print("Hay 1000 y es la tripleta A: {} , B: {} , C: {} ".format(listaA[num], listaB[num],listaC[num] ))                       
                        num = num + 1

                        
if __name__ == '__main__':
    #función que genera el algoritmo para la solución del problema
    encontrar_el_1000()

