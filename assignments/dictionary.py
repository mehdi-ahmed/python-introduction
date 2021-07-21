# input a number and transform numbers into letters
# example: 1234 = One Two Three Four

phone_number = input("Give a Phone number: ")
result = ""
numbers_dictionary = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero",
}

for number in phone_number:
    result += numbers_dictionary[int(number)] + " "

print(result)

# Mosh version
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in digits_mapping:
    output += digits_mapping.get(ch, "!") + " "  # in case it is not found, a "!" will be displayed

print(output)
