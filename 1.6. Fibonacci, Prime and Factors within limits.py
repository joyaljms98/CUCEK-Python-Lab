
# 6.a) Python program to generate Fibonacci series upto a given limit

'''
n = int(input("Enter the number of digits to display as fibonacci : "))
a = 0
b = 1
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("The Fibonacci sequence up to ", n, " digits is : ")
    print(a)
else:
    print("The Fibonacci sequence up to ", n, " digits is : ")
    print(a)
    print(b)
    for i in range(1,n-1):
        c = b+a
        print(c)
        a = b
        b = c
'''

# 6.b) Python program to generate Prime numbers between two given limit

'''
a = int(input("Enter a number as start of limit : "))
b = int(input("Enter a number as end of limit : "))
print("The prime numbers from ",a," to ",b," are ")
for i in range(a, b+1):
    C = 0
    for j in range(1,i+1):
        if i%j == 0:
            C = C+1
    if C == 2:
        print(i,end=", ")
'''

# 6.c) Python program to generate Factors of each number between two given limits

'''
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print()
for i in range (a, b+1):
        print(f"Factors of {i} : ")
        for j in range (1,i+1):
            if(i%j==0):
                print(j, end=',')
        print("\n")
'''
