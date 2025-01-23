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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

for num in numbers:
    print(num)
    
number = 0
while number < 10:
    number += 1
    print(number)

numbers_dict = {
    '1': 1, '2': 4, '3': 9, '4': 16,
    '7': 49, '8': 64, '9': 81, '10': 100
}

for key, val in numbers_dict.items():
    print(f'{key} => {val}')
    
# Part 4: Conditional Logic

#     Create a variable called temperature and set it to a number representing the current temperature 
#     (in degrees Celsius).
#     Using an if statement, print out a message telling the user whether they should wear a coat or not 
#     based on the current temperature. If the temperature is below 10 degrees Celsius, print out a message 
#     telling the user to wear a coat. If the temperature is 10 degrees Celsius or above, print out a message 
#     telling the user that they do not need to wear a coat.
#     Create a variable called username and set it to a string representing the user's username.
#     Using an if statement, print out a message telling the user whether their username is too long or not. 
#     If the username is more than 10 characters long, print out a message telling the user that their 
#     username is too long. If the username is 10 characters or less, print out a message telling the user 
#     that their username is okay.
#     Create a list called numbers_2 that contains the numbers 1 through 5.
#     Using a for loop and an if statement, print out only the even numbers in the numbers_2 list.

temperature = 10
if temperature >= 10:
    print('You dont need to wear a coat!')
else:
    print('You need to wear a coat!')
    
username = '5432112345'
if len(username) >= 10:
    print('Your username is okay')
else:
    print('Your username is too long')
    
numbers_2 = [1, 2, 3, 4, 5]

for num in numbers_2:
    if num % 2 == 0:
        print(num)