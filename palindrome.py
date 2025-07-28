num = int(input("Enter a number: "))#yh line user se input lerhi h
original =  num #store origina number for comparision later
rev = 0 #reverse number ko store krne ke liye variable

while num > 0: #reverse number niklne ke liye loop

    digit = num % 10 # last digit niklane ke liye % modules krne for example 123%10 = 3
    rev = rev * 10 + digit # reverse number ko update krne ke liye last digit ko add krte h for example 0*10 + 3 = 3, 3*10 + 2 = 32, 32*10 + 1 = 321
    num = num // 10 # number ko updae krne ke liye last digit ko remove krte h for example 123//10 = 12, 12//10 = 1, 1//10 = 0

if original == rev: #original number or reverse number ko compare krte h 
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
# yh program run krne ke liye terminal p python palindrome.py chlngye

# 787 > 0 
# digit = 787 % 10 = 7
# rev = 0 * 10 + 7 = 7
# num = 787 // 10 = 78

# 78 > 0
# digit = 78 % 10 = 8
# rev = 7 * 10 + 8 = 78
# num = 78 // 10 = 7

# 7 > 0
# digit = 7 % 10 = 7
# rev = 78 * 10 + 7 = 787
# num = 7 // 10 = 0

# 0 > 0 (loop ends)