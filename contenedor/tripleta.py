def encontrar_el_1000():
    listaA = list()
    listaB = list()
    listaC = list()
    lista_final = list()
    num = 0
    for p in range(30):
        for q in range(30):
            if p < q:
                if p > 0:
                    if q > 0:                     
                        listaA.append(p**2 + q**2)
                        listaB.append(2*p*q)
                        listaC.append(q**2 - p**2)
                        lista_final.append(listaA[num] + listaB[num] + listaC[num])
                        if lista_final[num] == 1000:
                            print("Hay 1000 y es la tripleta A: {} , B: {} , C: {} ".format(listaA[num], listaB[num],listaC[num] ))                       
                        num = num + 1

                        
if __name__ == '__main__':
    encontrar_el_1000()

