from idlelib.editor import keynames


def print_params(*params):  # *args, **kwargs
    print(params)
    print(*params)


print_params(1, 2, 3, 4, 5, 6, 7, 8, 9)
print_params()


def print_params(a, b, c):  # *args, **kwargs
    print(a, b, c)


list_ = [1, 2, 3]
print_params(list_, 2, 3)
print_params(*list_)


def print_params(a, b, c):  # *args, **kwargs
    print(a, b, c)


list_ = [1, 2]
print_params(list_, 2, 3)
print_params(4, *list_)


def print_params(a, b, c):  # *args, **kwargs
    print(a, b, c)


dict_ = {'a': 6, 'b': 7, 'c': 8}  # названия ключей должны соответствовать параметрам
print_params(**dict_)


def print_params4(**kwargs):  # *args, **kwargs
    for key in kwargs:
        print(key)
    for key, value in kwargs.items():
        print(key, value)


dict_ = {'a': 6, 'b': 7, 'd': 8}  # названия ключей должны соответствовать параметрам
print_params4(**dict_)


def print_params5(a, b, c):  # *args, **kwargs
    print(a, b, c)


list_1 = [1, 2]
dict_1 = {'c': 8}
print_params5(*list_1, **dict_1)
