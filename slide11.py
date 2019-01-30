##### Задание 2 #####
def razr(chislo1):
    chislo1 = abs(chislo1)
    count = 1
    chislo1 //= 10
    while chislo1 > 0:
        chislo1 //= 10
        count += 1
    return count

##### Задание 3 #####
def palindrom(s):
    return (s == s[::-1])

if __name__ == "__slide11__":
    chislo1 = int(input('Введите число '))
    print(razr(chislo1))
    s = input('Введите строку ')
    print(palindrom(s))