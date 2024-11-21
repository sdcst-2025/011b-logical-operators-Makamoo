#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

V = 'Guile'
V = 'Blanka'
V = 'Christine'
V = 'Carol'
V = 'Richard'
V = 'Daniel'
V = 'Chun-Li'

EHonda = input("VIP Room Guard: What's your name? ")

if EHonda == V:
    print(f"Hi {EHonda}! You are a VIP!")
else:
    print(f"Nice try {EHonda}, you are actually not a VIP, try again another time")