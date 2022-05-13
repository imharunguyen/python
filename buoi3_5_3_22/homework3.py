
#-------bai_1: tam giac can
a = int(input('Nhap canh a: '))
b = int(input('Nhap canh b: '))
c = int(input('Nhap canh c: '))

if a > 0 and b > 0 and c > 0 and a < b + c and b < a + c and c < a + b:
    if a == b or a == c or b == c:
        print('CAN')
    else:
        print('Thuong')
else:
    print('Tam giac khong hop le')

#-------bai_2: kiem tra gio, phut, giay
hour = int(input('Nhap gio: '))
minute = int(input('Nhap phut: '))
second = int(input('Nhap giay: '))

if 00 <= hour <= 23:
    if 0 <= minute <= 60:
        if 0 <= second <= 60:
            print(f'{hour}h {minute}m {second}s')
        else:
            print('Giay khong hop le')
    else:
        print('Phut khong hop le')
else:
    print('Gio khong hop le')

#-------bai_3: 
if 0 < a < 10 and 0 < b < 10 and 0 < c < 10:
    if a <= b <= c:
        print(f'{c}{b}{a}')
    elif a <= c <= b:
        print(f'{b}{c}{a}')
    elif b <= a <= c:
        print(f'{c}{a}{b}')
    elif b <= c <= a:
        print(f'{a}{c}{b}')
    elif c <= a <= b:
        print(f'{b}{a}{c}')
    else:  # c <= b <= a
        print(f'{a}{b}{c}')
else:
    print()

#-------bai_4: ax^2 + bx + c
import math

a = float(input('Nhap he so a: '))
b = float(input('Nhap he so b: '))
c = float(input('Nhap he so c: '))

if a == 0:
    if b == 0:
        if c == 0:
            print('Phuong trinh vo so nghiem')
        else:
            print('Phuong trinh vo nghiem')
    else:
        print('Phuong trinh bac 1 co nghiem x =', -c / b)
else:
    delta = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta < 0:
        print('Phuong trinh vo nghiem')
    elif delta == 0:
        x = -b / (2 * a)
        print(' Phuong trinh co nghiem kep x1 = x2 =', x)
    else:
        print('phuong trinh co 2 nghiem x1 =', x1, ',', 'x2 =', x2)
        
#-------bai_5: tinh cuoc xe
km = float(input('Nhap so KM: '))
pr1 = 15000
pr20 = 12000
pr21 = 10000

if km < 0:
    print('Do dai quang duong la so thuc duong')
else:
    if km < 1:
        print('Tong tien: ', pr1, 'VND')
    elif km <= 21:
        print('Tong tien: ', pr1 + pr20 * (km - 1), 'VND')
    else:
        print('Tong tien: ', pr1 + pr20 * 20 + (km - 21) * pr21, 'VND')