#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""
import math
Boo = float(input("Number is... "))

su = Boo/6
Goo = int(su)
chew = float(Goo)

if su == chew:
    doobytoo = True
else:
    doobytoo = False

New = Boo/8
YounghoeKoo = int(New)
joo = float(YounghoeKoo)

if New == joo:
    HobbyHorse = True
else:
    HobbyHorse = False

if doobytoo == True:
    if HobbyHorse == False:
        print(f"{Boo} is frue")
    else:
        print(f"{Boo} is not frue")
else:
    print(f"{Boo} is not frue")