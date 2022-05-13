

#--------------------------------
a = float(input('Nhap a: '))
b = float(input('NHap b: '))
if a == 0:
    if b == 0:
        print('phuong trinh vo so nghiem')
    else:
        print('phuong trinh vo nghiem')
else:
    print('phuong trinh co nghiem x = ', -b / a)

#----------so chinh phuong
import math

n = int(input('Nhap n: '))
if math.sqrt(n) == math.isqrt(n):
    print('yes')
else:
    print('no')

#----------kiem tra luy thua cua 2 
#có ít nhất 3 số 0 và ít nhất 1 số 1 
'''
10 = 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0
10 (hệ 10) = 1010 (hệ 2)

8  = 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0
8  (hệ 10) = 1000 (hệ 2)

7  = 0*2^3 + 1*2^2 + 1*2^1 + 1*2^0
7  (hệ 10) = 0111 (hệ 2)

4  = 0*2^3 + 1*2^2 + 0*2^1 + 0*2^0
4  (hệ 10) = 0100 (hệ 2)

print(8 & 7)    -> đổi ra hệ 1000 & 0111 = 0000
                (&: chỉ cần 1 False thì tất cả là False)
print(8 | 7) (in ra màn là 15)   
                -> đổi ra hệ 1000 | 0111 = 1111
                1111 = 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0 = 15
'''
n = int(input('Nhap n: '))
if n & (n - 1):
    print(n, 'la so chinh phuong')
else:
    print(n, 'khong la so chinh phuong')

#---------Bài luyện tập tổng hợp

#--------bai_1: tim so lon hon
a = float(input("Nhập a = "))
b = float(input("Nhập b = "))

if a > b:
    print('so lon hon la: ', a)
elif a == b:
    print('Hai so bang nhau')
else:
    print('So lon hon la: ', b)

#--------bai_2: sap xep so tang dan
a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
c = float(input('Nhap c: '))

if a <= b <= c:
    print(f'{a}  {b}  {c}')
elif a <= b <= c:
    print(f'{a}  {b}  {c}')
elif b <= a <= c:
    print(f'{b}  {a}  {c}')
elif b <= c <= a:
    print(f'{b}  {c}  {a}')
elif c <= a <= b:
    print(f'{c}  {a}  {b}')
else: # c <= b <= a
    print(f'{c}  {b}  {a}')

#--------bai_3:kiem tra tam giac
if a > 0 and b > 0 and c > 0 and a < b + c and b < a + b and c < a + b:
    print('tam giac hop le')
    if a == b == c:
        print('day la tam giac deu')
    elif a**2 == (b**2 + c**2) or b**2 == (a**2 + c**2)or c**2 == (a**2 + b**2):
        if a == b or b == c or a == c:
            print('Day la tam giac vuong can')
        else:
            print('Day la tam giac vuong')
else:
    print('Tam giac khong hop le')

#--------bai_4:
x = int(input('Nhap nam: '))
if x > 0:
    if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
        print(x, 'la nam nhuan')
    else:
        print(x, 'khong la nam nhuan')
else:
    print('Nam khong hop le')