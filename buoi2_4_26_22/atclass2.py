
#-------------------------bai_1
if __name__ == '__main__':
    a = eval(input('Nhap a: '))
    b = eval(input('Nhap b: '))
    print(a > b, a < b, a == b, a != b)
#-------------------------bai_2
if __name__ == '__main__':
    x = eval(input())
    print(x % 2 == 0)
#-------------------------bai_3
if __name__ == '__main__':
    x = int(input())
    print(x % 2 == 0)
    print(x > 22 and x < 44)
#-------------------------bai_4
if __name__ == '__main__':
    c = input('Nhap c: ')
    print(c >= '0' and c <= '9')
    print((ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')))
    print(32 < ord(c) <= 47 or 58 <= ord(c) <= 64)
    print(c == ' ')
#-------------------------bai_5
x = int(input('Nhap nam: '))
if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
    print(x, 'la nam nhuan')
else:
    print(x, 'khong la nam nhuan')






