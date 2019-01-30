##### Задание 1 #####
def list1(slovo):
    return ([i+3 for i in range(((len(slovo)%5) + 2) * 2)])
##### Задание 2 #####
def list2(slovo):
    list_of_v = [i + 3 for i in range(((len(slovo) % 5) + 2) * 2)]
    return (list_of_v + [i+1 for i in list_of_v])
##### Задание 3 #####
def list3(slovo):
    list_of_v = [i + 3 for i in range(((len(slovo) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    return (list2[1:-1])
##### Задание 4 #####
def list4(slovo):
    # list = []
    list_of_v = [i + 3 for i in range(((len(slovo) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    return ([list2[i] for i in range(1, len(list2), 3)])
##### Задание 5 #####

def list5(slovo):
    list_of_v = [i + 3 for i in range(((len(slovo) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    return ([list2[i] for i in range((n - 1) * round(len(list2) / 3), round(n * len(list2) / 3))])


if __name__ == '__main__':
    slovo = input('Введите фамилию: ')
    print(list1(slovo))
    print(list2(slovo))
    print(list3(slovo))
    print(list4(slovo))
    n = int(input('Введите часть списка для отображения: '))
    print(list5(slovo))