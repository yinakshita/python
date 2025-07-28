# for loop
num = int(input("Enter a number: "))  # user se input lerhi h
factorial = 1  # variable to store factorial, initialized to 1

for i in range(1, num + 1):  # loop from 1 to num
    factorial *= i  # multiply each number to get factorial
print(f"The factorial of {num} is: {factorial}")
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
# This program calculates the factorial of a number.
# To run this program, use the command: python factorial.py

num = int(input("Enter a number: "))  # user se input lerhi h
factorial = 1  # variable to store factorial, initialized to 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is: 1")
else:
    for i in range(1, num + 1):  # loop from 1 to num
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

#using recursion

def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call
    
num = int(input("Enter a number: "))  # user se input lerhi h
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is: 1")
else:
    print(f"The factorial of {num} is: {factorial(num)}")