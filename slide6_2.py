##### Задание 1 #####
def dict1(slovo):
    return ({i: i + 2 for i in range(((len(slovo) % 5) + 2) * 2)})
##### Задание 2 #####
def dict2(slovo):
    d = {i: i + 2 for i in range(((len(slovo) % 5) + 2) * 2)}
    d.update({i + len(d): d[i]+1 for i in range(len(d))})
    return d
##### Задание 3 #####
def dict3(slovo):
    d = {i: i + 2 for i in range(((len(slovo) % 5) + 2) * 2)}
    d.update({i+len(d): d[i]+1 for i in range(len(d))})
    return ({i: d[i] for i in range(1, len(d)-1)})
##### Задание 4 #####
def dict4(slovo):
    d = {i: i + 2 for i in range(((len(slovo) % 5) + 2) * 2)}
    d.update({i+len(d): d[i]+1 for i in range(len(d))})
    return ({i: d[i] for i in range(1, len(d), 3)})
##### Задание 5 #####
def dict5(slovo):
    d = {i: i + 2 for i in range(((len(slovo) % 5) + 2) * 2)}
    d.update({i+len(d): d[i]+1 for i in range(len(d))})
    return ({i: d[i] for i in range((n - 1) * round(len(d) / 3), round(n * len(d) / 3))})

if __name__ == '__main__':
    slovo = input('Введите фамилию: ')
    print(dict1(slovo))
    print(dict2(slovo))
    print(dict3(slovo))
    print(dict4(slovo))
    n = int(input('Введите часть словаря для отображения: '))
    print(dict5(slovo))

