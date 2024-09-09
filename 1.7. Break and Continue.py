
# 7.a) Python program to print First half numbers of a given limit using 'break'

'''

n = int(input("Enter a limit: "))
mid = n // 2
for i in range(1, n + 1):
    if i > mid:
        break
    print(i)
'''

# 7.b) Python program to print Even numbers upto a limit of 'n' using ' continue

'''
n = int(input("Enter a limit: "))
for i in range(1, n + 1):
    if i%2 == 0:
        print(i)
    else:
        continue
'''
