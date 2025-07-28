num = int(input("Enter a number: ")) # yh line user se input lerhi h
original = num # store original number for comparison later
sum = 0 # sum of cubes of digits ko store krne ke liye variable

while num > 0: # sum of cubes of digits niklne ke liye loop
    digit = num % 10 #last digit niklane ke liye % modules krne for example 123%10 = 3
    sum = sum + (digit ** 3)  # last digit ke cube ko sum me add krne ke liye
    num = num // 10 # number ko update krne ke liye last digit ko remove krte h 

if original == sum: # original number or sum of cubes of digits ko compare krte h
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
# yh program run krne ke liye terminal p python armstrong.py chlngye

# Example: 153

# 153 > 0
# digit = 153 % 10 = 3
# sum = 0 + (3 ** 3) = 27
# num = 153 // 10 = 15

# 15 > 0
# digit = 15 % 10 = 5
# sum = 27 + (5 ** 3) = 152
# num = 15 // 10 = 1

# 1 > 0
# digit = 1 % 10 = 1
# sum = 152 + (1 ** 3) = 153
# num = 1 // 10 = 0

# 0 > 0 (loop ends)