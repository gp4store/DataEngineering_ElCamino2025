import pandas as pd
import json

## Make sure the data files are in the same directory as the code or indicate the path to the datafile when opening
# it to read or write.

Bond = {'Father': 'James Bond', 'Mother': 'Maria Bond', 'Daughter': 'Consuela Bond', 'Son': 'Jack Bond'}

Hernandez = {'Father': 'Caesar Hernandez', 'Mother': 'Gloria Hernandez', 'Daughter': 'Lupe Hernandez',
             'Son': 'Carlito Hernandez'}

Nazari = {'Father': 'Ali Nazari', 'Mother': 'Samira Nazari', 'Daughter': '', 'Son': 'Abdi Nazari'}

Green = {'Father': 'Thomas Green', 'Mother': 'Claire Green', 'Daughter': 'Zoe Green', 'Son': ''}

Singh = {'Father': 'Amar Singh', 'Mother': 'Chuni Singh', 'Daughter': 'Greysi Singh', 'Son': 'Haashim Singh'}

families = [Bond, Hernandez, Nazari, Green, Singh]

# print(families)

"""TRY EXCEPT BLOCK EXAMPLE"""
try:
    file = open('new_families2.txt', 'r')

    for f in file:
        json_in = f.replace("'", '"')
        new_f = json.loads(json_in)

    print("This try-block worked!")


except IOError as e:
    print("Error in the try block, please fix this!")
    print(e)

finally:
    print("This runs no matter what.")
# file = open('new_families.txt', 'r')

# print(file) # <_io.TextIOWrapper name='new_families.txt' mode='r' encoding='UTF-8'>
# print(type(file)) # <class '_io.TextIOWrapper'>

# for f in file:
    # print(type(f)) # <class 'str'>
    # print(f)
    json_in = f.replace("'", '"')
    new_f = json.loads(json_in)
# print(new_f)
# print(type(new_f))


fam_list = families + new_f
# print(fam_list)
# """**************
# comprehensions
# # ***************"""
# """ A List Comprehension """
# print([d for d in fam_list])
# #
# """ Print fam_list list comprehension"""
# print([f for f in fam_list])
# # #
# """ Print each dictionary from the fam_list list comprehension"""
# [print(f) for f in fam_list]
# # #
# """ Print a nested dict comp from the list comp"""
# print([{k: v for k, v in f.items()} for f in fam_list])
# # # #
# """ Print a new list of dicts containing only the Father(s) and/or Mother(s)
# from the nested dict comp from the list comp"""
# print([{k: v for k, v in f.items() if k == 'Father' or k == 'Mother'} for f in fam_list])
# # #
# """ Print a new list of dicts containing only the extracted last name from either Father or Mother
# from the nested dict comp from the list comp"""
# print([{'Family_Name': v[v.index(' '):len(v)] for k, v in d.items() if k == 'Father' or k == 'Mother'} for d in fam_list])
""" Print a new list of dicts containing the extracted last name as a new key/value pair from either Father or Mother
joined to the nested dict comp for each family dict in the fam_list comp"""
fams = [{**{'Family_Name': (v[v.index(' ')+1:len(v)]) for k, v in d.items() if k == 'Father' or k == 'Mother'}, **d} for d in fam_list]
# [print(d) for d in fams]

#
# # #
family_l = []
for d in fams:
# for d in fam_list:
    adults = 0
    children = 0
    for k in d:
        if 'Father' in k or 'Mother' in k:
            adults = adults + 1
        else:
            children = children + 1
    d['Adults'] = adults
    d['Children'] = children
    family_l.append(d)
    # print(d)
# # #
"""Read the address.csv for the variable, "add_file":"""
add_df = pd.read_csv('addresses.csv', header=0)
# print(add_df)
# # #
"""Create pandas DataFrames for each, family data and address data:"""
family_df = pd.DataFrame(data=family_l)
# print(family_df)
# # # # #
"""Merge the two pandas DataFrames together, joining on the "Family_Name" column:"""
family_data = pd.merge(family_df, add_df)
# # # # #
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(family_data)
# # # #
"""Write the family_data DataFrame out to a comma seperated value file, 'family_data.csv'"""
family_data.to_csv('family_data.csv', index=None)
# # # # #
