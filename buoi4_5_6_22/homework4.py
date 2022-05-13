# github: https://github.com/imharunguyen/python-core

#------ kiểm tra số nguyên tố
import math

n = int(input('Nhap n: '))
check = 1
if n <= 1:
    print(n, 'khong la so nguyen to')
else:
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            check = 0
            print(n, 'khong la so nguyen to')
            break
        else:
            check = 1
if check == 1:
    print(n, 'la so nguyen to')

#------Đường chéo từ trái sang phải của hình vuông cỡ n 
rows = int(input('Nhap n: '))
for i in range(rows):
    for j in range(rows):
        if i == 0 and j == 0 or j == i:
            print('*', end=' ')
        else:
            print('0', end=' ')
    print()

#------Đường chéo từ phải sang trái của hình vuông cỡ n 
rows = int(input('Nhap n: '))

for i in range(rows):
    for j in range(rows):
        if i + j == rows - 1:
            print('*', end=' ')
        else:
            print('0', end=' ')
    print()

#------ Tính S = 1 + 1/(1+2) + .. + 1/(1+2+..+n)
n = int(input('Nhap n: '))
s = 0

for i in range(1, n + 1):
    s += 2 / (i * (i + 1))
print(s)

#------ liệt kê số nguyên tố
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))

if a >= b:
    print('Khong hop le')
else:
    for i in range(a + 1, b):
        if i > 1:
            for x in range(2, i):
                if i % x == 0:
                    break
            else:
                print(i, end=' ')


