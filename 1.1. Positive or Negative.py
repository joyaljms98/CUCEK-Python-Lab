
# 1.a) Python program to check whether a given number is Positive or negative using if-else

'''
n = int(input("Enter a number to check if positive or negative : "))
if n < 0:
    print(n," is Negative")
else:
    print(n," is Positive")
'''



# 1.b) Python program to check whether a given number is Positive, negative or zero using if-elif-else

'''
n = int(input("Enter a number to check if positive, negative or zero : "))
if n < 0:
    print(n," is Negative")
elif n == 0:
    print("Number entered is Zero")
else:
    print(n," is Positive")
'''



# 1.c) Python program to check whether a given number is Positive, negative or zero using nested if

'''
n = int(input("Enter a number to check if positive, negative or zero : "))
if n >= 0:
    if n>0:
        print(n," is Positive")
    else:
        print("Number entered is Zero")
else:
    print(n," is Negative")
'''
