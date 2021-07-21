# remove duplicates in a list
a_list = [4, 5, 8, 4, 8, 9, 12, 47, 5, 47, 965, 5, 8]
uniques = []
for item in a_list:
    if item not in uniques:
        uniques.append(item)

print(uniques)
# [4, 5, 8, 9, 12, 47, 965]

