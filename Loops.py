if __name__ == '__main__':
    n = int(input())

lista = []

if n <=20 and n >=1:
    for numero in range(0,n):
        lista.append(numero*numero)
        print(lista[numero])
