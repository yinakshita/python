n = int(input("Enter the number of terms: "))
sum_n = n * (n + 1) // 2  # sum of first n natural numbers
print(f"The sum of the first {n} natural numbers is: {sum_n}")
print("sum of first", n , "natural numbers is:", sum_n)
#formula: n(n+1)/2

#for loop 

sum_n = 0
for i in range(1, n + 1):
    sum_n += i  # add each number to the sum
print(f"The sum of the first {n} natural numbers is: {sum_n}")
print("sum of first", n , "natural numbers is:", sum_n)
