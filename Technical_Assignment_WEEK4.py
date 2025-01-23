# Part 1: Lists

#     Create a list called shopping_list that contains at least 5 items you need to buy at the grocery store.
#     Print out the third item in shopping_list.
#     Add two more items to the end of shopping_list.
#     Remove the first item from shopping_list.
#     Print out the final version of shopping_list., 

shopping_list = ['eggs', 'milk', 'bread', 'cheese', 'chicken']

print(shopping_list[2])

shopping_list.append('beef')
shopping_list.append('tomatoes')
print(shopping_list)

shopping_list.remove('eggs')
print(shopping_list)

print(shopping_list)

# Part 2: Dictionaries

#     Create a dictionary called my_info that contains your name, age, and favorite hobby.
#     Print out your name from the my_info dictionary.
#     Update the value of your favorite hobby in the my_info dictionary.
#     Add a new key-value pair to the my_info dictionary that contains your favorite food.
#     Print out the final version of the my_info dictionary.


my_info = {
    'name': 'Gerardo Pastore',
    'age':  '32',
    'hobby': 'crossfit'
}

print(my_info['name'])

my_info['hobby'] = 'Olympic Weighlifing'
print(my_info)

my_info['food'] = 'pupusas'
print(my_info)

# Part 3: Loops

#     Create a list called numbers that contains the numbers 1 through 10.
#     Using a for loop, print out each number in the numbers list.
#     Using a while loop, print out each number in the numbers list.
#     Create a dictionary called squares that contains the squares of the numbers 1 through 5 (e.g. 1: 1, 2: 4, 3: 9, 4: 16, 5: 25).
#     Using a for loop, print out each key-value pair in the squares dictionary.

