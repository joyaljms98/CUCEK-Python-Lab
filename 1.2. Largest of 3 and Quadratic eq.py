
# 2.a) Python program to find Largest of 3 numbers(using if-elif.. ladder)

'''
a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
c = int(input("Enter Third number : "))
if a>b and a>c:
    large = a
elif b>a and b>c:
    large = b
else:
    large = c
print(large, " is greatest")
'''



# 2.b) Python program to find Largest of 3 numbers(using nested if)

'''
a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
c = int(input("Enter Third number : "))
if a>b:
    if a>c:
        large = a
    else:
        large = c
else:
    if b>c:
        large = b
    else:
        large = c
print(large," is greatest")
'''


# 2.c) Python program to find Nature of roots of quadratic equation

'''
a = int(input("Enter Second coefficient : "))
b = int(input("Enter First coefficient : "))
c = int(input("Enter constant term : "))
discriminant = b*b - 4*a*c
if discriminant > 0:
    print("The roots are real and distinct")
elif discriminant == 0:
    print("The roots are real and equal")
else:
    print("The roots are imaginary")
'''
