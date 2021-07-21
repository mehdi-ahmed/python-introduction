is_hot = False
is_cold = True

if is_hot:
    print('It is a hot day !!')
elif is_cold:
    print('I love cold days!')
else:
    print('I love average days!')

# Indentation is important !!

# and or

has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print('Eligible to a Loan AND')

if has_high_income or has_good_credit:
    print('Eligible to a Loan OR')

if has_high_income or not has_criminal_record:
    print('Eligible to a Loan NOT')
