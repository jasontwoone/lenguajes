
N, M = map(int, input().split(' '))

if N>=5 and N<= 101 and N%2 != 0:
    if 15>=15 and M<= 303 and 3*N == M:
        for valor in range(1,N,2):
            print((valor * '.|.').center(M,'-'))
        print('WELCOME'.center(M,'-'))
        for valor in range(N-2,-1,-2):
            print((valor *('.|.')).center(M,'-'))
