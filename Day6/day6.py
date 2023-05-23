# Write a Python program to remove duplicates from a list.

def remove_duplicates(lst):
    return list(set(lst))

# Example usage:
my_list = [1, 2, 3, 3, 4, 5, 5, 6, 6, 2]
unique_list = remove_duplicates(my_list)
print(unique_list)

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#  Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
# Expected Output : ['Green', 'White', 'Black']

def remove_elements(lst, indices):
    for index in sorted(indices, reverse=True):
        del lst[index]
    return lst

# Example usage:
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices_to_remove = [0, 4, 5]
modified_list = remove_elements(sample_list, indices_to_remove)
print(modified_list)

# Write a Python program to check if each number is prime in a given list of numbers.
#  Return True if all numbers are prime otherwise False.
#  Sample Data: ([0, 3, 4, 7, 9]) -> False ([3, 5, 7, 13]) -> True ([1, 5, 3]) -> False

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_all_primes(nums):
    for num in nums:
        if not is_prime(num):
            return False
    return True

# Example usage:
data_1 = [0, 3, 4, 7, 9]
data_2 = [3, 5, 7, 13]
data_3 = [1, 5, 3]

print(check_all_primes(data_1))  
print(check_all_primes(data_2))  
print(check_all_primes(data_3))  

