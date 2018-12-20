# Author:  Edward Moradian

Num = input("Please give an integer: ")
Num = int(Num)

if Num > 0:
    print("Your number is positive")
elif Num == 0:
    print("Your number is zero")
else:
    print("Your number is negative")
    
if Num % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")