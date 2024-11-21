#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
import math

Frederico = int(input("enter a number but the catch is it needs to be an integer "))
Anthony = int(input("another one "))
Warner = int(input("another one(last one) "))

if Frederico == Anthony or Frederico == Warner or Anthony == Warner:
    print("Don't put two of the same number or it wont work dummy, I didn't mention this before but how am i supposed to put your integers in order if they are the same?!")
    exit()
Brock = max(Frederico, Anthony, Warner)
Purdy = min(Frederico, Anthony, Warner)
QB1 = Frederico + Anthony  + Warner - Brock - Purdy

if Brock == math.sqrt(Purdy**2 + QB1**2):
    print(f"{Frederico}, {Anthony} and {Warner} form a pythagorean triple")
else:
    print(f"{Frederico}, {Anthony} and {Warner} DO NOT form a pythagorean triple, try again LOSER!")