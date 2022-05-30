
'''
Nhập số n nguyên dương.
1 Khai báo list a rỗng
2 Nhập vào từ bàn phím n số, lưu vào list a
3 Lặp qua các phần tử của a. In ra:
Số lớn nhất - vị trí của nó. Số nhỏ nhất - vị trí của nó
Tổng - tích các phần tử
Chạy bằng tay từng dòng code theo dữ liệu nhập vào. Thêm print để
kiểm nghiệm kết quả
'''
n = int(input('Nhap n = '))
a = []
s = 0
mul = 1
for i in range(n):
    val = int(input(f'Nhap gia tri: '))
    a.append(val)
max_val = a[0]
min_val = a[0]
for i in range(0, len(a)):
    s += a[i]
    mul *= a[i]
    if a[i] < min_val:
        min_val = a[i]
    if a[i] > max_val:
        max_val = a[i]
print('Tong la: ', s)
print('Tich la: ', mul)
print(f'So lon nhat la {max_val} vi tri la {a.index(max_val)}')
print(f'So nho nhat la {min_val} vi tri la {a.index(min_val)}')

'''
Viết chương trình
1 Nhập vào mảng các số nguyên, có số phần tử n
2 In ra tất cả vị trí của các phần tử trong mảng có giá trị x, với x được
nhập vào từ bàn phím. Nếu không có, in ra -1
3 In ra vị trí đầu tiên từ trái sang phải của phần tử có giá trị x. Nếu
không có, in ra -1. Tương tự với phần tử tính từ phải sang trái
4 Tìm phần tử chẵn cuối cùng trong mảng, nếu không có , in ra -1
'''
lst = list(map(int, input('Nhap mang: ').split()))
x = int(input('Nhap x = '))
equalto_x = []
even_val = []
'''
res = [i for i, v in enumerate(lst) if v == x]
print(res)
'''
check_x = 0
check_even = 0
for i, v in enumerate(lst):
    if v == x:
        equalto_x.append(i)
    else:
        check_x += 1
temp_lst = lst[::-1]
for i in temp_lst:
    if i % 2 == 0:
        even_val.append(i)
    else:
        check_even += 1
if check_x == len(lst):
    print(-1)
else:
    print(f'Cac vi tri cua phan tu trong mang co gia tri {x} la {equalto_x}')
    print(f'Tu trai sang phai vi tri cua phan tu dau tien trong mang co gia tri {x} la {equalto_x[0]}')
if check_even == len(lst):
    print(-1)
else:
    print(f'Phan tu chan cuoi cung trong mang la {even_val[0]}')

'''
Viết chương trình:
1 Đếm số phần tử chẵn trong mảng n phần tử nguyên được nhập vào
từ bàn phím
2 Đếm số phần tử chính phương trong mảng trên
3 Đếm số phần tử có giá trị x, với x nhập vào từ bàn phím
4 Đếm số phần tử có giá trị <= x
'''
import math

lst = []
n = int(input('Nhap n = '))
x = int(input('Nhap x = '))
count_even, count_sqr_num = 0, 0
count_eqto_x, count = 0, 0

for i in range(n):
    val = int(input('Nhap gia tri '))
    lst.append(val)

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        count_even += 1
    if math.sqrt(lst[i]) == math.isqrt(lst[i]):
        count_sqr_num += 1
    if lst[i] == x:
        count_eqto_x += 1
    if lst[i] <= x:
        count += 1
print(f'So phan tu chan la {count_even}')
print(f'So phan tu chinh phuong la {count_sqr_num}')
print(f'So phan tu co gia tri {x} la {count_eqto_x}')
print(f'So phan tu co gia tri <= {x} la {count}')

'''
Ma trận có thể biểu diễn bằng một list của list. Viết chương trình:
Nhập vào một ma trận các số thực cỡ m * n với m, n nhập vào từ
bàn phím
In ra ma trận đó
Phép nhân ma trận với 1 số là nhân số đó với từng phần tử trong ma
trận. Hãy thực hiện nhân ma trận đó với n, với n nhập vào từ bàn
phím và in ra kết quả
'''
lst = []
m = int(input('Nhap m hang: '))
n = int(input('Nhap n cot: '))
x = int(input('Nhap x = '))
for i in range(m):
    lst.append([])
    for j in range(n):
        val = int(input(f'Nhap phan tu hang {i + 1} cot {j + 1}: '))
        lst[i].append(val)
print(f'lst = {lst}')
for i in range(m):
    for j in range(n):
        lst[i][j] *= x
print(f'lst sau = {lst}')










