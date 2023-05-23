# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers,
#  adding up to a target number.

import itertools

def find_combinations(numbers, target):
    combinations = []
    for combination in itertools.combinations(numbers, 3):
        if sum(combination) == target:
            combinations.append(combination)
    return combinations

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 10

combinations = find_combinations(numbers, target)
print(combinations)

# Write a Python program to return a new set with unique items from both sets by removing duplicates.
#  Given: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
# Expected output: {70, 40, 10, 50, 20, 60, 30}

def combine_sets(set1, set2):
    combined_set = set1.union(set2)
    return combined_set

# Example usage:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

combined_set = combine_sets(set1, set2)
print(combined_set)

# Update the first set with items that don’t exist in the second set Given two Python sets, 
# write a Python program to update the first set with items that exist only in the first set and
#  not in the second set. Given: set1 = {10, 20, 30} set2 = {20, 40, 50} Expected output: set1 {10, 30}

def update_set(set1, set2):
    set1.difference_update(set2)

# Example usage:
set1 = {10, 20, 30}
set2 = {20, 40, 50}

update_set(set1, set2)
print(set1)
