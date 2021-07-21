try:
    age = int(input("Age ?: "))
    income = 2000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value, please insert Integers only')
except ZeroDivisionError:
    print('Age should not equal to 0')
