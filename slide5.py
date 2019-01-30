def count_math(x, y, z, w):
    return (((x * (y - x)) / z) + x + ((w + z) / (w ** y)) - ((z - w) / z)) / (((z + w )/ z ** y) - w)

if __name__ == '__slide5__':
    x = int(input('Введите x : '))
    y = int(input('Введите y : '))
    z = int(input('Введите z : '))
    w = int(input('Введите w : '))
    print(count_math(x, y, z, w))