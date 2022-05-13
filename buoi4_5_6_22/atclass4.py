# Vòng lập for - cấu trúc lập xác định

# ------------ Ví dụ
n = int(input('Nhap n: '))
for i in range(1, n + 1):
    print(i)

# ------------ Ví dụ
n = int(input())
for i in range(1, n + 1):
    print('Hello World', i)

# hàm range
# range([started=0], stop, [step=1])

#------ Tính n!
n = int(input('Nhap n: '))
s = 1
for i in range(1, n + 1):
    s *= i
print(s)

#------- Tính S = 1^2 + 2^2 + ... + n^2
n = int(input('Nhap n: '))
s = 0
for i in range(1, n + 1):
    s += i**2
print(s)

#--------
n = int(input('Nhap n: '))
s = 0
for i in range(n + 1):
    if i % 2 != 0:
        s += i
        print(s)
print('Tong cac so le la', s)

#--------
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
even = 0
odd = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('so cac so chan la:', even)
print('so cac so le la:', odd)

#--------
n = int(input('Nhap n: '))
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('Uoc cua', n, 'la', i)
        cnt += 1
print('So cac uoc cua', n, 'la', cnt)

#--------
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
s = 0
for i in range(a + 1, b):
    if i % 2 != 0:
        print(i)
    if i % 5 == 0:
        s += i
print('Tong cac so chia het cho 5 la', s)

#------ Tính S = 1 + 1/(1+2) + .. + 1/(1+2+..+n)
'''
1/(1+2+..+n) = 1/[n(n+1)/2] = 2/[n(n+1)] =
= [2(n+1-n)] / [n(n+1)] = 2*[1/n -1/(n+1)]

S1 = 2*[1/1 -1/(1+1)]
S2 = 2*[1/2 -1/(2+1)]
=> Sn = 2n/(n+1)
'''
# ------- nếu không dùng for
n = int(input('Nhap n: '))
s = 2 * n / (n + 1)
print(s)
# ------- nếu dùng for
n = int(input('Nhap n: '))
s = 0

for i in range(1, n + 1):
    s += 2 / (i * (i + 1))
print(s)