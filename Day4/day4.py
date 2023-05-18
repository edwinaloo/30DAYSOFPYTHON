# 1.write a function in python that takes a list of 
# numbers and returns the sum of the given numbers. 

# 2. write a function in python that takes a list of
#  numbers and returns the second-largest item in the list 

#  3. write a function in python that takes 3 parameters:
#  name, age, and occupation and prints this sentence as
#  output: "My name is {name}, I am {age} years old and 
# I work as a {occupation}". 


numbers = [1, 2, 3, 4, 5]

def add_numbers(numbers):
    total = sum(numbers)
    return total

result = add_numbers(numbers)
def find_second_largest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[1]
    return second_largest

print(numbers)
print(result)
print("Second largest number:", find_second_largest(numbers))

def print_person_info(name, age, occupation):
    print(f"My name is {name}, I am {age} years old, and I work as a {occupation}")


print_person_info("Edwin", 17, "Software Engineer")









