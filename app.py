# 1---------Inputs and concatenation--------

name = input('What is your name? ')
color = input('What is favorite color? ')

print(name + ' likes ' + color)

# 2---------Type conversion- Error -------

birth_year = input('Birth year ? ')
age = 2021 - birth_year
print(age)
# this will cause "TypeError: unsupported operand type(s) for -: 'int' and 'str'

# Fix
age = 2021 - int(birth_year)
print(age)

# Types explained
type_demo = input('Just write anything number ')
# <class 'str'>
print(type(type_demo))

# <class 'int'>
print(type(int(age)))