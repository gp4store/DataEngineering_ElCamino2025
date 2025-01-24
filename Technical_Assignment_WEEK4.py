#     All modules need to be imported at the very top of every script
import json

# Part 1: Lists

#     Create a list called shopping_list that contains at least 5 items you need to buy at the grocery store.
#     Print out the third item in shopping_list.
#     Add two more items to the end of shopping_list.
#     Remove the first item from shopping_list.
#     Print out the final version of shopping_list., 

shopping_list = ['eggs', 'milk', 'bread', 'cheese', 'chicken']
 
#     Slicing the list at index 2 so item 3 gets printed to screen
print(shopping_list[2])

#     Using append list method to add, beef and tomatoes at the end of the list
shopping_list.append('beef')
shopping_list.append('tomatoes')
print(shopping_list)

#     Removed first item of the list by using the list method remove
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

#     Using index slicing on key 'name' so the value link to the key gets printed to screen
print(my_info['name'])

#     Changing the value from the key using slicing
my_info['hobby'] = 'Olympic Weighlifing'
print(my_info)

#     Inserting new key, value to my_info dictionary through slicing
my_info['food'] = 'pupusas'
print(my_info)

# Part 3: Loops

#     Create a list called numbers that contains the numbers 1 through 10.
#     Using a for loop, print out each number in the numbers list.
#     Using a while loop, print out each number in the numbers list.
#     Create a dictionary called squares that contains the squares of the numbers 1 through 5 (e.g. 1: 1, 2: 4, 3: 9, 4: 16, 5: 25).
#     Using a for loop, print out each key-value pair in the squares dictionary.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

#     Iteraring over numbers list and printing each item in list
for num in numbers:
    print(num)
    
#     Setting a variable to zero to avoid an infinite loop, using += operator to keep printing the items 
#     in numbers list until the value reaches 10
number = 0
while number < 10:
    number += 1
    print(number)

numbers_dict = {
    '1': 1, '2': 4, '3': 9, '4': 16,
    '7': 49, '8': 64, '9': 81, '10': 100
}

#   Using the dictionary method items so the key, value gets print to screen after each interation

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


#     Using Python conditional logic operators to establish relations and conditional logic

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
        
# Part 5: Wrangling Data 

#     Read the 'new_families.txt' file (included in your materials) into memory and assign the variable, 
#     “file” to the object.
#     Print(file) # Can you read the data in the file?
#     What is the datatype of the file variable?
#     Write a FOR loop to iterate over the Text IO object referenced by the file variable and print each 
#     iteration of the text. How many results did you get back? #HINT shouldn't be a very large number ;)
#     What is the datatype of the object returned in the iteration?
#     What happens when you try to parse the first item in the list?
#     Change the string variable into a list of dictionaries type so you can work with it. #HINT: import json
#     Now that you have a list, print only the second item from the list. What is its type?


#     Read the 'new_families.txt' file (included in your materials) into memory and assign the variable, 
#     “file” to the object.
file = open('new_families.txt', 'r')
for i in file:
#     Iterating over the file object created, using type print result showed <class str>
    print(type(i))
    print(i)
    

#     Change the string variable into a list of dictionaries type so you can work with it. #HINT: import json
#     Now that you have a list, print only the second item from the list. What is its type?

for item in file:
#     Since the object returned is a string using replace method to replace double quotes for singles
#     so item can be interpreted for the json module
    json_in = item.replace("'", '"')
    new_file = json.loads(json_in)
    
print(new_file)
print(type(new_file))

#     Now that you have a list, print only the second item from the list. What is its type?
#     Using type to print the datatype, using list slicing/indexing to select just the 2nd dict in the list
print(type(new_file[1]))