n = int(input("Enter a positive integer: "))

fibonacci = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

for i in range(2, n):
    next_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_num)
# Fibonacci: Write a program that prompts the user to 
# enter a positive integer n, and then prints the first 
# n Fibonacci numbers. The Fibonacci sequence starts 
# with 0 and 1, and each subsequent number is the sum of
#  the two preceding numbers.

def fibonacci(n):
    sequence = [0, 1]  
    # Initialize the Fibonacci sequence with the first 
    # two numbers

    for i in range(2, n):
        # Calculate the next Fibonacci number as the 
        # sum of the previous two numbers
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence[:n] 
 # Return only the first n Fibonacci numbers


# Prompt the user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Call the fibonacci function and print the result
fib_numbers = fibonacci(n)
print("Fibonacci sequence:")
for num in fib_numbers:
    print(num)


# In this program, the fibonacci function takes a parameter n representing the number of Fibonacci numbers to generate. 
# It uses a list sequence to store the Fibonacci sequence, starting with the first two numbers 0 and 1. 
# It then iterates from index 2 up to n and calculates each subsequent 
# Fibonacci number by summing the previous two numbers. 
# The function returns a slice of the sequence containing only the first n Fibonacci numbers.












    

