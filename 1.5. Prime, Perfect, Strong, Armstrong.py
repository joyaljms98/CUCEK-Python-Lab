
# 5.a) Python program to check whether number is Prime or not

'''
C = 0
n = int(input("Enter a number to check if prime : "))
for i in range(1,n+1):
    if n%i == 0:
        C = C+1
if C == 2:
    print("Is prime")
else:
    print("Is not Prime")
'''

# 5.b) Python program to check whether number is Perfect or not   - eg: 6=1+2+3, 28=1+2+4+7+14, 496, 8128, 33550

'''
C = 0
n = int(input("Enter a number to check if perfect : "))
for i in range(1,n):
    if n%i == 0:
        C=C+i
if C == n:
    print("Is perfect number",C)
else:
    print("Is not perfect number", C)
'''

# 5.c) Python program to check whether number is Strong number or not   - eg 145 = 1! + 4! + 5!

'''
j=0
strg = 0
n = int(input("Enter a number to check if strong : "))
x = n
while (x!=0):
    j = x%10
    fac = 1
    for i in range(1, j+1):
        fac = fac*i
    x = x//10
    strg = strg+fac
print("Input Number = ",n, "\nSum of Factorials = ", strg)
if strg == n:
    print("Hence ",n," is a strong number")
else:
    print("Hence ",n," is not strong number")
'''

# 5.d) Python program to check whether number is Armstrong number or not   - eg 153 = 1^3 + 5^3 + 3^3

'''
c=0
arm = 0
n = int(input("Enter a number to check if strong : "))
x = n
while (x!=0):
    x = x//10
    c=c+1
x = n
while (x!=0):
    j = x%10
    j=j**c
    arm = arm+j
    x = x//10
print("Input number = ",n, "\nSum of powers = ", arm)
if arm == n:
    print("Hence ",n," is an armstrong number")
else:
    print("Hence ",n," is not armstrong number")
'''
