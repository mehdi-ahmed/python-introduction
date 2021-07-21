# 3---------Strings -------
course = '''
Hey guys ! You're awesome
Goodbye !!!
'''
print(course)

another_course = 'This is a Python course'
print(another_course[5])
# output = i

print(another_course[-1])
# output = e

print(another_course[-2])
# output = s

print(another_course[0:5])
# output = This

print(another_course[0:])
# output = This is a Python course

print(another_course[:2])
# output = Th  -- Python will assume 0 at start index

another_string = 'Jennifer'
print(another_string[1:-3])
# output = enni

# Formatted strings
first = 'Mehdi'
last = 'Ahmed'
msg = f'{first} [{last}] is a coder'
print(msg)
# Mehdi [Ahmed] is a coder

# String functions
course = 'This is a Python course'
print(len(course))
# 23

print(course.upper())
# THIS IS A PYTHON COURSE

print(course.find('P'))
# 10

print(course.replace('Python', 'Java'))
# This is a Java course

print('Python' in course)
# True
print('python' in course)
# False
print('jython' in course)
# False

print('hey hey'.title())
# Hey Hey -- Make the first letter in each word upper case
