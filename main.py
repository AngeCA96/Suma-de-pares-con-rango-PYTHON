def obtenerValor(texto):
    try:
        valor=int(input(texto))
    except:
        return 0
    return valor
 
while True:
    valorInicial=obtenerValor("Ingresa el valor inicial: ")
    valorFinal=obtenerValor("Ingresa el valor final: ")
 
    if valorInicial<valorFinal:
        break
    else:
        print("El valor inicial tiene que ser inferior al valor final ")
 
suma=sum([i for i in range(valorInicial,valorFinal+1) if i%2==0])
 
print("Numero Inicial: {}".format(valorInicial))
print("Numero Final: {}".format(valorFinal))
print("La suma de los numeros pares es: {}".format(suma))
