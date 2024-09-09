
# 4.a) Python program to find Factorial of a number

'''
n = int(input("Enter a number to find its factorial : "))
print(f"Factorial of {n} is : ")
fac = 1
for i in range(1, n+1):
    fac = fac * i
print(fac)
'''

# 4.b) Python program to find Factors of a number

'''
n = int(input("Enter a number to find the factors : "))
print(f"Factors of {n} are : ")
for i in range(1, n+1):
    if (n%i == 0):
        print(i, end = ",")
'''

# 4.c) Python program to find Prime factors of a number

'''
n = int(input("Enter a number to find the Prime factors : "))
print(f"Prime Factors of {n} are : ")
for i in range(1, n+1):
    if (n%i == 0):
        c=0
        for j in range(1, i+1):
            if (i%j == 0):
                c+=1
        if(c==2):
            print(i)
'''

# 4.d) Python program to find LCM and GCD of two given numbers

'''
a = int(input("Enter First Number : "))
b = int(input("Enter First Number : "))
if (a>b):
    large = a
    small = b
else:
    large = b
    small = a
while(1):
    if (large % a == 0 and large % b == 0):
        LCM = large
        break
    large = large+1
print(f"LCM of {a} and {b} is : {LCM}")

for i in range (1,small+1):
    if (a % i == 0 and b % i == 0):
        GCD = i
print(f"GCD of {a} and {b} is : {GCD}")
'''
