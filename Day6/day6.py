# Write a Python program to combine two dictionary by adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400} 
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter

def combine_dictionaries(d1, d2):
    result = Counter(d1)
    result.update(d2)
    return result

# Example usage
d1 = {'a': 90, 'b': 200, 'c': 380}
d2 = {'a': 200, 'b': 200, 'd': 500}
combined_dict = combine_dictionaries(d1, d2)
print(combined_dict)

# combine_dictionaries function takes two dictionaries (d1 and d2) as input. It creates a Counter object named result initialized with the elements of d1. The Counter class is a subclass of a dictionary that allows easy counting of elements.

# Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string. Sample string : 
# 'w3resource' Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

def create_letter_count(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 2
        else:
            letter_count[letter] = 2
    return letter_count

# Example usage
sample_string = 'w3resource'
result = create_letter_count(sample_string)
print(result)

# it create_letter_count function takes a string as input. It initializes an empty dictionary letter_count to store the count of each letter.

# The function then iterates over each character in the string using a for loop. For each letter, it checks if the letter already exists as a key in the letter_count dictionary using the in operator.

 # Write a Python program to sort Counter by value.
#  Sample data : {'Math':81, 'Physics':83, 'Chemistry':87} Expected data:
#  [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

from collections import Counter

def sort_counter_by_value(counter):
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

# Example usage
data = {'General Education': 50, 'Physical Education': 89, 'Mental Destruction': 100}
sorted_data = sort_counter_by_value(data)
print(sorted_data)

#  sort_counter_by_value function takes a Counter object (counter) as input. It uses the items() method of the Counter object to get a list of key-value pairs.


