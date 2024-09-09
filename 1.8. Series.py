
# 8.a) Python program to find Exact middle digit/s of a number (not half)

'''
n = int(input('Enter a number: '))
x = n
c1 = 0
c2 = 0
while(x!=0):
    x = x//10
    c1 += 1
x = n
print("Exact middle digit/s is : ")
while(x!=0):
    x = x // 10
    c2 += 1
    if(c1%2 != 0 and c2 == (c1//2)+1):                # if odd
        d = n//(10**(c1-c2))%10
        print(d)
        break
    elif c1 % 2 == 0 and (c2 == (c1 // 2) or c2 == (c1 // 2) + 1):             # if even
        d = n // (10 ** (c1 - c2)) % 10
        print(d)
'''

# 8.b) Python program to find Sum of series: 1 - 1/2 + 1/4 - 1/8 + ...

'''
n = int(input('Enter a limit for the length of series : '))
sum = 0
for i in range(0,n):
    sum = sum + ((-1)**i * (1/(2**i)))
print("sum is : ",sum)
'''

# 8.c) Python program to find Sum of series: x + (x^2)/4 + (x^3)/9 + ...

'''
n = int(input('Enter a limit for the series : '))
x = int(input("Enter the value of x: "))
sum = 0
for i in range(1, n+1):
    sum = sum + ((x ** i) / (i ** 2))
print("Sum is ", sum)
'''

# 8.d) Python program to find Sum of series: (x^2)/2 + (x^3)/3 + (x^5)/5 + (x^7)/7 + ...     
# recheck

'''
n = int(input('Enter a limit for the series : '))
x = int(input("Enter the value of x: "))
sum = 0
term_count = 0
current_prime = 2    # Start with the first prime number

while term_count < n:    # Function to check if a number is prime
    # Check if the current number is prime
    is_prime = True
    for i in range(2, int(current_prime ** 0.5) + 1):
        if current_prime % i == 0:
            is_prime = False
            break

    if is_prime:       # If the number is prime, add the corresponding term to the series
        term = (x ** current_prime) / current_prime
        sum += term
        term_count += 1

    current_prime += 1

print(f"The sum of the series for {n} terms is: {sum}")
'''
