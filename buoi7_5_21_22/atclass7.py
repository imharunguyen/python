#------------Luyện Tập---------------

'''
Nhập 1 số tự nhiên n - yêu cầu nhập lại đến 
khi đúng thì thôi (n int,
n > 0)
Tiếp đó nhập n số nguyên.
In ra tổng các phần tử trong dãy, 
in ra tích các số lẻ trong dãy
'''

result_sum = 0
result_sum_str = ''
result_mul_odd = 1
result_mul_odd_str = ''
while True:
    n = int(input('Nhap n = '))
    if n > 0:
        break
    else:
        print('Nhap sai, Nhap lai.')

for i in range(n):
    x = int(input('Nhap so: '))
    result_sum += x
    if result_sum_str != '':
        result_sum_str += ' + '
    result_sum_str = f'{result_sum_str}{x}'

    if x % 2 != 0:
        result_mul_odd *= x
        if result_mul_odd_str != '':
            result_mul_odd_str += ' . '
        result_mul_odd_str = f'{result_mul_odd_str}{x}'
print(result_sum_str, '=', result_sum)
print(result_mul_odd_str, '=', result_mul_odd)

#---------------------OR
while True:
    n = int(input('Nhập vào 1 số nguyên:'))
    if n > 0:
        break
    else:
        print(n, 'không hợp lệ, yêu cầu nhập lại\n')

print('Số phần tử cần nhập vào là:', n)

result_tong = 0
result_tich_le = 1
sum_trace = ''
for i in range(n):
    # print('-----------')
    current_input = int(input(f'Nhập vào số thứ {i + 1} '))

    if i == 0:
        sum_trace += str(current_input) + ' ' # = '3'
    else:
        if current_input > 0:
            current_trace = '+ ' + str(current_input)
        elif current_input < 0:
            # 5 + -8 = 5 - 8
            current_trace = '- ' + str(- current_input)  
        sum_trace += current_trace + ' '

    result_tong = result_tong + current_input
    if current_input % 2:  # so le
        result_tich_le *= current_input
    # print(sum_trace, result_tong)

#print(result_tong, result_tich_le)
print(sum_trace, '=', result_tong)

'''
Nhập vào số tự nhiên x
In ra vị trí các phần tử trong dãy nhập vào có giá trị <= x, nếu
không có, in ra "Không có giá trị = ..." trong dãy nhập vào
In ra vị trí các phần tử trong dãy nhập vào có giá trị = x, nếu không
có, in ra "Không có giá trị = ..." trong dãy nhập vào
'''
while True:
    n = int(input('Số phần tử cần nhập vào: '))

    if n > 0:
        break
    else:
        print(n, 'không hợp lệ, yêu cầu nhập lại\n')

x = int(input('Nhap so nguyen x: '))
lessthan_equalto_x_ind = ''
equal_to_x_ind = ''
for i in range(n):
    val = int(input(f'Nhap so thu {i + 1}: '))

    if val <= x:
        lessthan_equalto_x_ind += str(i + 1) + ' '

        if val == x:
            equal_to_x_ind += str(i + 1) + ' '

if lessthan_equalto_x_ind:
    print(lessthan_equalto_x_ind)
else:
    print(-1)
print('------------------------')
if equal_to_x_ind:
    print(equal_to_x_ind)
else:
    print(-1)

'''
In ra vị trí của phần tử đầu tiên có giá trị = x, phần tử cuối cùng có
giá trị = x
'''
#---- phần tử cuối = x: (vd x = 2, 1 2 2 3 4 2 7)
#                                            | ptu vtr cuối
while True:
    n = int(input('Số phần tử cần nhập vào: '))
    if n > 0:
        break
    else:
        print(n, 'không hợp lệ, yêu cầu nhập lại\n')

x = int(input('Nhap so nguyen x: '))    
last_equalto_x_ind = -1
for i in range(n):
    val = int(input(f'Nhap so thu {i + 1}: '))

    if val == x:
        last_equalto_x_ind = i + 1
print('Vi tri cuoi = x:', last_equalto_x_ind)

#---- phần tử đầu = x: (vd x = 2, 1 2 2 3 4 2 7)
#                                   | ptu vtr đầu
while True:
    n = int(input('Số phần tử cần nhập vào: '))
    if n > 0:
        break
    else:
        print(n, 'không hợp lệ, yêu cầu nhập lại\n')

x = int(input('Nhap so nguyen x: '))    # x = 2
first_equalto_x_ind = 0
for i in range(n):
    val = int(input(f'Nhap so thu {i + 1}: '))

    if val == x:
        first_equalto_x_ind = i + 1
        break
print('Vi tri dau tien = x:', first_equalto_x_ind)

'''
ƯỚC CHUNG LỚN NHẤT, BỘI CHUNG NHỎ NHẤT
'''
#---------------UCLN
while True:
    a = int(input('Nhap a: '))
    b = int(input('Nhap b: '))
    if a > 0 and b > 0:
        break
    else:
        print('Nhap lai')
while b != 0:
    r = a % b
    a = b
    b = r
print(a)

#---------------BCNN
while True:
    a = int(input('Nhap a = '))
    b = int(input('Nhap b = '))
    if a > 0 and b > 0:
        break
    else:
        print('Nhap sai. Nhap lai \n')
temp_a, temp_b = a, b
while temp_a != temp_b:
    if temp_a > temp_b:
        temp_a -= temp_b
    else:
        temp_b -= temp_a
lcm = (a * b) // temp_a
print(f'BCNN cua {a} va {b} la {lcm}')

"""
Nhập vào 1 ký tự, nếu gặp enter thì chuyển sang bước tiếp theo
In ra tổng các ký tự là số trong chuỗi ký tự đã nhập
"""

s = 0
while True:
    c = input('Nhap 1 ki tu: ')
    
    if c == '':
        break
    if len(c) > 1:
        print('Nhap sai. Nhap lai')
        continue
    if '0' < c < '9':
        s += int(c)
print(s)

'''
aAbcAAAAc####123 ----> aabcaaaac
-----
(0) -> nếu là chữ cái hoa -> chuyển về chữ cái thường
(1) -> với các chữ cái thường -> thêm vào kết quả
'''

s = 0
result = ''
while True:
    c = input('Nhap 1 ki tu: ')

    if c == '':
        break
    if len(c) > 1:
        print('Nhap sai. Nhap lai')
        continue
    if '0' < c < '9':
        s += int(c)

    if 'A' <= c <= 'Z':
        c = chr(ord(c) + 32)  # đưa vào bảng mã ascii
        # chuyển chữ hoa thành chữ thường

    if 'a' <= c <= 'z':
        result += c
print(s)
print('------------')
print(result)

'''
2. Một số được gọi là số bậc thang nếu 
biểu diễn thập phân của nó có nhiều hơn một chữ số 
đồng thời theo chiều từ trái qua phải, 
chữ số đứng sau không nhỏ hơn chữ số đứng trước.  
Viết chương trình  
- Nhập vào 2 số nguyên dương a, b (9 < a < b). 
Yêu cầu người dùng nhập tới khi đúng 
- In ra các số bậc thang trong đoạn [a, b] 
-------------------------
a = 133
b = 150
->  134 135 136 137 138 139 145 146 147 148 149
'''
while True:
    a = int(input('Nhap a = '))
    b = int(input('Nhap b = '))
    if 9 < a < b:
        break
    else:
        print('Nhap sai. Nhap lai \n')
for i in range(a, b + 1):   # i=134
    temp_i = i      # temp = 134
    temp = i % 10   # temp= 4
    i = i//10   # i=13
    if temp > (i % 10):    # 4 > (13 % 10 = 3)
        print(temp_i, end=' ')