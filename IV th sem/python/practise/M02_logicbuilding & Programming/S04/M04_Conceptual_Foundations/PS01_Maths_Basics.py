a = int(input())
b = int(input())
min_num = min(a,b)
gcd = 1
for i in range(1,min_num+1):
    if a%i==0 and b%i==0:
        gcd = i
print(gcd)
#solution 2
min_num = min(a,b)
gcd = 1
for i in range(1,min_num+1):
    if a%i==0 and b%i==0:
        gcd = i
print(gcd)
#solution 3
while b != 0:
    a, b = b, a % b
print(a)