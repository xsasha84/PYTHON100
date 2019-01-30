import random
chislo_igr = 2
chislo_poytok = 5
igr = 0
popytka = 0
snova = 'да'
while snova == 'да':
    igr += 1
    chislo = random.randint(1, 100)
    print(chislo)
    vvod_polz = input('Введите число ')
    while not (vvod_polz.isdigit()):
        print('Не число!')
        vvod_polz = input('Введите число ')
    vvod_polz = int(vvod_polz)
    popytka += 1
    while vvod_polz != chislo:
        if vvod_polz < chislo:
            print('надо больше!')
            vvod_polz = input('Введите число ')
            while not (vvod_polz.isdigit()):
                print('Не число!')
                vvod_polz = input('Введите число ')
            vvod_polz = int(vvod_polz)
            popytka += 1
        elif vvod_polz > chislo:
            print('надо меньше!')
            vvod_polz = input('Введите число ')
            while not (vvod_polz.isdigit()):
                print('Не число!')
                vvod_polz = input('Введите число ')
            vvod_polz = int(vvod_polz)
            popytka += 1
        if popytka == chislo_poytok:
            break
    if igr == chislo_igr and popytka != chislo_poytok and chislo == vvod_polz:
        print('Угадано! Сыграно 2 игры! Конец игры!')
        snova = 'нет'
    elif popytka == chislo_poytok and igr != chislo_igr and chislo == vvod_polz:
        print('Угадано! Израсходованы все попытки! Конец игры')
        snova = 'нет'
    elif popytka == chislo_poytok:
        print('Не угадано! Израсходованы все попытки! Конец игры')
        snova = 'нет'
    else:
        print("Угадано!")
        snova = input('Хотеите сыграть ещё?\nВведите да или нет ')
