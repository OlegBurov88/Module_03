def print_params(a=1, b=2, c=3):
    print(a, b, c)


print_params("1", 2, True)
print_params(c='srt')
print_params()
print_params(1, 6, c=7.9)
print_params(c=False, a=8, b='ok')


def print_params2(*, a, b, c):  #все что идет после «*» в функции, мы должны конкретно указать
    print(a, b, c)


print_params2(c=False, a=8, b='ok')  #все что идет после «*» в функции, мы должны конкретно указать
# print_params2(1, 2, 3)  #все что идет после «*» в функции, мы должны конкретно указать
