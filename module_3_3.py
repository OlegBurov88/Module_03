def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['str', False, 5]
values_dict = {'a': False, 'b': 5, 'c': 'str'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)


"""
Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
def a(my_list = [])) – это приводит к ошибкам!

Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
def append_to_list(item, list_my=None):
  if list_my is None:
   list_my = []
  list_my.append(item)
print(list_my)
"""