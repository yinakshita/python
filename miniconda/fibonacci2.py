n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=' ')
    c = a + b  # next term is the sum of the last two terms
    a = b  # update a to the last term
    b = c  # update b to the new term
    count += 1  # increment the count

# Example: 0 1 1 2 3
# This will print the first 5 terms of the Fibonacci sequence.
# This program prints the first n terms of the Fibonacci sequence.
# To run this program, use the command: python fibonacci.py


n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=' ')
    c = a + b  # next term is the sum of the last two terms
    a = b  # update a to the last term
    b = c  # update b to the new term