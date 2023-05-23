# Write a Python program to combine two dictionary by adding values for common keys.
#  d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400}
#  Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter

def combine_dictionaries(d1, d2):
    combined_dict = Counter(d1)
    combined_dict.update(d2)
    return combined_dict

# Example usage:
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dictionaries(d1, d2)
print(combined_dict)

 # Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string. Sample string : 'w3resource' 
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

def create_dictionary(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

# Example usage:
my_string = "hello"

dictionary = create_dictionary(my_string)
print(dictionary)

# Write a Python program to sort Counter by value.
#  Sample data : {'Math':81, 'Physics':83, 'Chemistry':87} Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

from collections import Counter

def sort_counter_by_value(counter):
    sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    sorted_counter = {k: v for k, v in sorted_items}
    return sorted_counter

# Example usage:
counter = Counter({'Math':81, 'Physics':83, 'Chemistry':87})

sorted_counter = sort_counter_by_value(counter)
print(sorted_counter)

