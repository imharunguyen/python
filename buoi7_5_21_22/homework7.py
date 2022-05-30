
'''
1. Số chính phương là số có căn bậc 2 là 1 số nguyên. 
Viết chương trình 
- Nhập vào hai số nguyên dương a, b (0 < a < b). 
Yêu cầu người dùng nhập tới khi đúng. 
- Liệt kê các số chính phương trong khoảng [a;b] 
'''
import math

while True:
    a = int(input('Nhap a = '))
    b = int(input('Nhap b = '))
    if 0 < a < b:
        break
    else:
        print('Nhap sai. Nhap lai \n')

for i in range(a, b + 1):

    if math.sqrt(i) == math.isqrt(i):
        # print(f'math.sqrt: {math.sqrt(i)}')
        # print(f'math.isqrt: {math.isqrt(i)}')
        print(i, end=' ')

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
for i in range(a, b + 1):   
    temp_i = i      
    temp = i % 10  
    i = i//10   
    if temp > (i % 10):    
        print(temp_i, end=' ')

'''
3. Viết chương trình nhập vào hai số nguyên dương n, k 
- Nếu số chữ số của n lớn hơn hoặc bằng k, 
in ra k chữ số đầu tiên của n 
- Ngược lại, in ra một số mới ghép từ hai số n và k   
'''
while True:
    n = int(input('Nhap n = '))
    k = int(input('Nhap b = '))
    if n > 0 and k > 0:
        break
    else:
        print('Nhap sai. Nhap lai \n')
temp_n = n
count = 0
while n > 0:
    temp = n % 10
    count += 1
    n //= 10
if count >= k:
    print(str(temp_n // (10**(count - k))))
else:
    print(f'{temp_n}{k}')