 # Write a Python program to count the number of characters 
# (character frequency) in a string. Sample String : google.com' 
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def count_character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# usage
sample_string = 'google.com'
result = count_character_frequency(sample_string)
print(result)

    # The function initializes an empty dictionary frequency to store the character frequencies.

    # It then iterates through each character in the input string using a for loop.

    # For each character, it checks if the character already exists as a key in the frequency dictionary using the in operator.

    # If the character is already present in the dictionary, it increments the count of that character by 1 by using the += operator.

    # If the character is not yet in the dictionary, it adds a new key-value pair to the frequency dictionary, with the character as the key and an initial count of 1.

    # Finally, the function returns the frequency dictionary containing the character frequencies.

# Write a Python program to get a string made of the first 2 and last 2
#  characters of a given string. If the string length is less than 2, 
# return the empty string instead. Sample String : 'w3resource' Expected Result :
#  'w3ce' Sample String : 'w3' Expected Result : 'w3w3' Sample String : ' w' Expected 
# Result : Empty String

def get_first_and_last_two_chars(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]

# Example usage
sample_string1 = 'w3resource'
result1 = get_first_and_last_two_chars(sample_string1)
print(result1)

sample_string2 = 'w3'
result2 = get_first_and_last_two_chars(sample_string2)
print(result2)

sample_string3 = ' w'
result3 = get_first_and_last_two_chars(sample_string3)
print(result3)

    # The function first checks if the length of the input string is less than 2 using the len() function. If it is, it means the string is too short to extract the desired characters, so it returns an empty string.

    # If the length of the string is greater than or equal to 2, the function uses string slicing to extract the first two characters (string[:2]) and the last two characters (string[-2:]).

    # It then concatenates the extracted substrings and returns the resulting string.


# Write a Python program to add 'ing' at the end of a given string
#  (length should be at least 3). If the given string already ends with 'ing', 
# add 'ly' instead. If the string length of the given string is less than 3, 
# leave it unchanged. Sample String : 'abc' Expected Result : 'abcing' Sample String 
# : 'string' Expected Result : 'stringly'

def modify_string(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'

# Example usage
sample_string1 = 'abc'
result1 = modify_string(sample_string1)
print(result1)

sample_string2 = 'string'
result2 = modify_string(sample_string2)
print(result2)

    # The function first checks if the length of the input string is less than 3 using the len() function. If it is, it means the string is too short to modify, so it returns the string unchanged.

    # If the length of the string is greater than or equal to 3, the function checks if the last three characters of the string (string[-3:]) are equal to 'ing'. If they are, it means the string already ends with 'ing', so it concatenates 'ly' to the string and returns the modified string.

    # If the last three characters of the string are not 'ing', it means the string does not end with 'ing', so it concatenates 'ing' to the string and returns the modified string.