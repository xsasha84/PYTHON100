##### Задание 1-2 #####
def posledov(N,M):
    fib = [1 for _ in range(M)]
    while len(fib) <= N:
        f = 0
        for i in range(1, M + 1):
            f += fib[-i]
        fib.append(f)
    return fib
##### Задание 3 #####
def kvadrat(n):
    return [n**2 for n in range(1, n+1, 2)]
##### Задание 4 #####
def ramka(shir,vis):
    s = '*'
    for i in range(vis+1):
        if i == 0 or i == vis:
            print(s*shir)
        else:
            print(s + ' '*(shir-2) + s)
##### Задание 5 #####
def vichisl(a,b):
    summa = 0
    proizv = 1
    for i in range(a,b + 1):
        summa += i
        proizv *= i
    return (summa, proizv)
##### Задание 6 #####
def chetnost(a,b):
    chet = []
    nechet = []
    for i in range(a,b+1):
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    return chet, nechet
##### Задание 7 #####
a = [1, 2, -3, 30, -50, 40, -2]
def znak(a):
    pol = []
    otr = []
    pol = [i for i in a if i >= 0]
    otr = [i for i in a if i < 0]
    return pol, otr

if __name__ == "__slide9__":
    N = int(input('Введите N '))
    M = int(input('Введите M '))
    print(posledov(N, M))
    n = int(input('введите число '))
    print(kvadrat(n))
    shir = int(input('Введите ширину: '))
    vis = int(input('Введите высоту: '))
    print(ramka(shir, vis))
    a = int(input('Введите число А: '))
    b = int(input('Введите число В: '))
    print(vichisl(a, b))
    a = int(input('Введите число А: '))
    b = int(input('Введите число В: '))
    print(chetnost(a, b))
    print(znak(a))