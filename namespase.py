a = 5
b = 10  # глобальные имена


def printer():
    global a, b  # Использование в локальном пространстве глобальных переменных
    a = 'str'
    b = 'str 2'
    c = 15
    d = 20
    print(c, d, 'local')  # локальные имена
    print(a, b, 'global')


print(a, b)
printer()
print(a, b)
