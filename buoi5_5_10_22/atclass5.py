'''
1
22
333
4444
55555
'''
rows = int(input('Nhap n: '))

for i in range(1, rows+1):
    print(f'{str(i) * i}')

#-----------------------------
i = 1000
e10, e100, e1000 = 0, 0, 0
gth = 1
for j in range(1, 1001):
    gth *= j
    if j == 10:
        e10 += 1 / gth
    if j == 100:
        e100 += 1 / gth
    if j == 1000:
        e1000 += 1 / gth
print(e10)
print(e100)
print(e1000)

#-----------------------------
import math

n = int(input('Nhap vao so n: '))
s = 0

for i in range(2, math.isqrt(n) + 1):
    is_prime = 1
    if n % i == 0:
        break
    else:
        s += i
print(s)

#-----------------------------
