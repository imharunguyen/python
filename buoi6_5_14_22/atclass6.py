'''
        vòng lặp không xác định - while
'''
#--in ra số tu2f 1 đến 15 bằng while
i = 1
while i <= 15:
    print(i, end=' ')
    i += 1

#--Nhập vào N, tính tổng các số lẻ từ 1- N sử dụng vòng lặp while
n = int(input('Nhap n: '))
i = 1
s = 0
while i <= n:
    if i % 2 != 0:
        s += i
    i += 1
print(s)

#--tính số e
threshold = 0.0000001
e, i, factorial = 1, 1, 1

while (1 / factorial) > threshold:
    factorial *= i
    e += 1 / factorial
    print(f'i = {i}, 1/i! = {1 / factorial}, e = {e}')
    i += 1

print(e)

#--
n = int(input('Nhap n: '))
while n != 0:
    print(n % 10, end='')
    n //= 10

#--------------
n = int(input('n = '))
binary = ''
while n > 0:
    k = n % 2
    #print(f'k = {k}')
    binary = str(k) + binary
    #print(f'x = {x}')
    n //= 2
    #print(f'nsau = {n}')
print(f'He nhi phan: {binary}')

temp = int(binary)
re_binary = ''
while temp != 0:
    print(f"temp = {temp}")
    re_binary += str(temp % 2)
    print(f're = {re_binary}')
    temp //= 10
    print(f'tempsau = {temp}')

print(f'Dao nguoc he nhi phan: {re_binary}')


'''
Decimal, i = 0, 0
binary1 = int(binary)
while binary1 != 0:
    dec = binary1 % 10
    Decimal = Decimal + dec * pow(2, i)
    binary1 //= 10
    i += 1
print(f'So nhi phan dao nguoc trong he 10: {Decimal}')
'''


