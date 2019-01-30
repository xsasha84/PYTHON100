##### Задание 1 #####
def stroka (n, s = ' akjsdhk'):
    return n*s
##### Задание 2 #####
def lesenka(n):
    st = '='
    for i in range(0, n + 1):
        print(st * i * 3)
##### Задание 3 #####
def kolbukv(inp_str):
    bukv = {}
    for sim in inp_str:
        if sim in bukv:
            bukv[sim] += 1
        else:
            bukv[sim] = 1
    return bukv
##### Задание 4 #####
def dlina(inp_predl):
    slov_dl = {}
    for word in inp_predl.split():
        key = 'слов длинной ' + str(len(word))
        if key in slov_dl:
            slov_dl[key] += 1
        else:
            slov_dl[key] = 1
    return slov_dl

if __name__ == "__slide7__":
    print(stroka(5))
    print(lesenka(7))
    inp_str = input('Введите строку: ')
    print(kolbukv(inp_str))
    inp_predl = input('Введите предложение: ')
    print(dlina(inp_predl))
