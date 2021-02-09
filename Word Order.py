
n = int(input())



lista=[]
listaPalabrasEncontradas=[]
cantidadDePalabras =[]

if n>=1 and n <=10**5:
    for valor in range(0, n):
        a=(input())
        if a.islower:
            lista.append(a)

for valor in range(0, len(lista)):
    if listaPalabrasEncontradas.count(lista[valor])==0:
        listaPalabrasEncontradas.append(lista[valor])
        cantidadDePalabras.append(lista.count(lista[valor]))
    
print(len(listaPalabrasEncontradas))
print(*cantidadDePalabras, sep=' ')
