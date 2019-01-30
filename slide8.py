##### Задание 1 #####
def beg1(km):
    res = 0
    den = 0
    while res < km:
        den += 1
        res += 2**den
    return den
##### Задание 2 #####
def beg2(km, n = 100):
    lst = []
    d = 0
    res = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            lst.append(i)
    while res < km:
        res += lst[d]
        d += 1
    return d
##### Задание 3 #####
def beg3(d, s = 10):
    res = 0
    n = 1
    while n <= d:
        if n % 2 == 0:
            s *= 1.15
        res += s
        n += 1
    return round(res,3)
##### Задание 4.1 #####
def beg4(km,s = 10):
    d = 1
    while s <= km:
        s *= 1.1
        d += 1
    return d
##### Задание 4.2 #####
def beg5(km, s = 10):
    res = 0
    d = 1
    while res <= km:
        res += s
        s *= 1.1
        d += 1
    return d

if __name__ == "__main__":
    print(beg1(1000))
    print(beg2(1000))
    print(beg3(10))
    print(beg4(15))
    print(beg5(100))