var_str = '"I have to learn Python"'
var_int = 42
var_float = 42.42
var_bytes = bytes('Bytes are everywhere', 'UTF-8')
var_list = list('мой список')
var_tuple = ('курсы', 'питон', 'Вадим')
var_set = {'fish', 'chips', 'pub', 'Hooligans'}
var_frzset = frozenset(var_set)
var_dict = dict(model='Low D Whistle', maker='Karavaev', price=7000)

print(var_str, 'Type of var_str: ', type(var_str))
print(var_int, 'Type of var_int: ', type(var_int))
print(var_float, 'Type of var_float: ', type(var_float))
print(var_bytes, 'Type of var_bytes: ', type(var_bytes))
print(var_list, 'Type of var_list: ', type(var_list))
print(var_tuple, 'Type of var_tuple: ', type(var_tuple))
print(var_set, 'Type of var_set: ', type(var_set))
print(var_frzset, 'Type of var_frzset: ', type(var_frzset))
print(var_dict, 'Type of var_dict: ', type(var_dict))

slogan1 = ('АМКАР - ')
slogan2 = ('чемпион!')
sloganTotal = slogan1 + slogan2
print(sloganTotal)

a = 18
b = 4
c = a + b
print(c)
d = a / b
print(d)
e = a * b
print(e)
f = a // b
print(f)
g = a % b
print(g)

expr = ((7 + 12)**3 + 7 * 4 - 44 / 2**4)
print(expr)

