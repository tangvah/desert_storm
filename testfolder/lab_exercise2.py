# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:17:13 2025

@author: CDAC
"""

# Q1. Create a string containing both a single quote and  double quote.
string = "This is a string containing single quote Don't go there! "
string2 = """(This is a string containing double quote, "Python is fun !")"""

# Q2. Create a triple quoted string that contains single and double quotes.
string_with_quotes = """This string contains a single quote (') and a double quote (")."""
print(string_with_quotes)

# Q3. Create a character, then obtain its integer representation.
char = 'A'
ascii_value = ord(char)
print(f"The integer representation of the given character {char} is {ascii_value}")

# Q4. Create a single string containing 5 copies of the string 'abc'.
string = 'abc'
copies = string * 5
print (copies)

# Q5 Use the multiplication operator to create a "line" of 50 dashes. 
char = '-'
line = char * 50
print(line)

# Q6. Convert a string to all upper case.
string = "Hello World"
stringUpper = string.upper()
print (stringUpper)

# Q7 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
def first_and_last_2_chars(input_string):
    # Check if the input string has at least 2 characters
    if len(input_string) < 2:
        return "Input string must have at least 2 characters"
    # Create the new string with the first 2 and last 2 characters
    new_string = input_string[:2] + input_string[-2:]
    return new_string

# Example usage
input_string = input("Enter a string: ")
result = first_and_last_2_chars(input_string)
print("The new string is:", result)

# Q8. Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def replace_char(input_string):
    first_char = input_string[0]
    replace_string = first_char + input_string[1:].replace(first_char, '$')
    return replace_string
# Main program
input_string = input("Please enter your text: ")
result = replace_char(input_string)
print(result)

# Q9 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
'''
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
'''
sample_str1 = 'abc'
sample_str2 = 'xyz'

def swap_str(str1,str2):
    swapstr1 = str2[:2] + str1[2:]
    swapstr2 = str1[:2] + str2[2:]
    combine_str = swapstr1 + ' ' + swapstr2
    return combine_str

str1 = input("Enter Text: ")
str2 = input("Enter Text: ")
result = swap_str(str1, str2)
print(f"The combine string result is : {result}")