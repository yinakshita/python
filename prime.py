num = int(input("Enter a number: "))#yh line user se input lerhi h 

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2,num): #prime number humesha se 2 se shuru hote h isliye range m likha h 2 agye  2 se phle vle jese 0,1 or negative numbers ko prime consider nhin kiya jat h
                          # 2 se lekar num tak check karega ki koi bhi number divide ho raha h ya nhin
                          # range me suppose kro num =7 toh range li jyegi 2,3,4,5,6 kyuki 7 include nhin hota h isliye range liya h or 7 include nh krne ka reason h kyuki 7 se toh 7 divisible hi h 
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number.")
                # yh program run krne ke liye terminal p python prime.py chlngye 
