# Write a program that declares a variable and assigns a string to it, then prints the variable.

text = 'Hello'
print(text)

# Write a program that declares two variables and concatenates them into a single string, then prints the result.

text1 = 'Hello'
text2 = ' World!'
result = text1 + text2
print(result)

# Write a program that declares a variable and prints the length of the string assigned to the variable.

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(len(alphabet))

# Write a program that declares a variable and prints the first letter of the string assigned to the variable.

text3 = 'Data_Engineering'
text4 = text3[0]

print(text4[0:])

# Write a program that declares a variable and prints the last letter of the string assigned to the variable.

text5 = 'Data_Engineering'
text6 = text5[-1:]

print(text6)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, from the 2nd to the 5th character.

text7 = 'Data_Engineering'
text8 = text7[1:5]
print(text8)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, from the 5th character to the end.

text9 = 'Data_Engineering'
text10 = text9[4:]
print(text10)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, from the 2nd to the 5th character in reverse order.

text11 = 'Data_Engineering'
text12 = text11[1:5][::-1]
print(text12)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, every other character.

text13 = 'Data Engineering'
text14 = text13[::2]
print(13)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, skipping the first two characters.

text15 = 'Data_Engineering'
text16 = text15[0::2]
print(text16)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, skipping the last two characters.

text17 = 'Data_Engineering'
text18 = text17[:-2]
print(text18)

# Write a program that declares a variable and prints a slice of the string assigned to the variable, skipping the first and last two characters.

text19 = 'Data_Engineering'
text20 = text19[2:-2]
print(text20)

# Write a program that declares a variable and converts the string assigned to the variable to all uppercase letters.

text21 = 'Data_Engineering'
text22 = text21.upper()
print(text22)

# Write a program that declares a variable and converts the string assigned to the variable to all lowercase letters.

text23 = 'Data_Engineering'
text24 = text23.lower()
print(text24)

# Write a program that declares a variable and replaces a portion of the string assigned to the variable with a new string.

text25 = 'Data_Engineering'
text26 = text25.replace('Engineering', 'Analysis')
print(text26)

