def greet_user():  # Best practices for functions: Starts with lower letters separated by a '_'
    print('Hi there !')
    print('Welcome aboard !')


print("Start")
greet_user()
print("Finish")


# Parameters
def greet_user(name):
    print(f'Hi there {name} !')
    print('Welcome aboard !')


print("Start")
greet_user('Mehdi')
greet_user('Sophie')
print("Finish")


# Functions with keyword arguments - Better readability:
# calc_price(50, 5, 0.01) vs calc_price(price=50, shipping=5, discount=0.01)
def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name} !')
    print('Welcome aboard !')


print("Start")
greet_user(last_name='Ahmed', first_name='Mehdi')  # We don't care about arguments' positions.
print("Finish")


#  !!! Position arguments should always come after regular arguments
#  greet_user(last_name='Ahmed', 'Mehdi') = Error
#  greet_user('Mehdi', last_name='Ahmed') = OK.

# Return statement
def square(number):
    return number * number


results = square(3)
print(results)  # 9
