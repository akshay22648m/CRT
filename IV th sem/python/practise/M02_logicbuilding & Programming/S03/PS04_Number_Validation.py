'''Armstrong number:
input: 153
output: 153 is an Armstrong number
input: 24
output: 24 is not an Armstrong number'''
'''
n = int(input("Enter a number: "))
count = len(str(n))
sum = 0
for i in str(n):
    s += int(i)**count
if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")'''
'''n = int(input())
s = 0
for i in range(1,n//2+1):
    if n%i == 0:
        s += i

print("perfect number" if s == n else "not a perfect number")'''
'''strong number:
input:123
out:not a strong number'''
def factorial(n):
    if n < 0:
        return "no factorial for -ve"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact
n = int(input())
s = 0
for digit in str(n):
    s += factorial(int(digit))
print("strong number" if s == n else "not a strong number")      
                   