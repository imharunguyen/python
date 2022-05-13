#github : https://github.com/thienthanhnguyen/python_core_turing

#------------------------------
x = int(input('Nhap x: '))
if x % 2 == 0:
    print(x, 'la so chan')
else:
    print(x, 'la so le')
if x > 22 and x < 44:
    print(x, 'nam trong khoang 22-44')
else:
    print(x, 'khong nam trong khoang 22-44')
#------------------------------------------
c = input('Nhap c: ')
if c >= '0' and c <= '9':
    print(c, 'la so')
elif ord('a') <= ord(c) <= ord('z'):
    print(c, 'la chu cai thuong')
elif ord('A') <= ord(c) <= ord('Z'):
    print(c, 'la chu hoa')
elif 32 < ord(c) <= 47 or 58 <= ord(c) <= 64:
    print(c, 'la ki tu dac biet')
elif c == '':
    print(c, 'la dau ENTER')
#------------------------------------------
x = int(input('Nhap nam: '))
if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
    print(x, 'la nam nhuan')
else:
    print(x, 'khong la nam nhuan')
#------------------------------------------
n = int(input('Nhap N: '))
if n == 0:
    print('N = 0')
elif n % 2 == 0:
    print(n, 'la so chan')
else:
    print(n, 'la so le')
#------------------------------------------
n = int(input('Nhap N: '))
if n < 0:
    print(n, 'la so am')
    print('Gia tri tuyet doi cua', n, ':', -n)
else:
    print('N >= 0')
    print('Gia tri tuyet doi cua', n, ':', n)

#----------ax^2 + bx + c = 0--------------
import math

a = float(input('Nhap he so a: '))
b = float(input('Nhap he so b: '))
c = float(input('Nhap he so c: '))
if a == 0:
    print('Phuong trinh bac 1 có nghiem x =', -c / b)
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('Phuong trinh vo nghiem')
    elif delta == 0:
        print(' Phuong trinh co nghiem kep x1 = x2 =', -b / (2 * a))
    else:
        print('phuong trinh co 2 nghiem')
        print('x1 =', (-b + math.sqrt(delta)) / (2 * a))
        print('x2 =', (-b - math.sqrt(delta)) / (2 * a))

#----------tinh cuoc taxi--------------
km = eval(input('Nhap so km da di: '))
if km <= 1:
    print('gia cuoc la: ', 15000)
elif km <= 21:
    print('Gia cuoc la: ', 15000 + (km - 1) * 12000)
else:
    print('Gia cuoc la: ', 15000 + 20 * 12000 + (km - 21) * 10000)
