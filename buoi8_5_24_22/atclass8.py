'''
            LIST
-------------------------------------------

- len(l) trả về số phần tử của list
- l.append(element) Đưa 1 phần tử vào cuối list
- l.insert(index, element) Đưa phần tử element vào vị trí index
- l1.extend(l2) Có tác dụng tương đương l1 + l2


    
'''
#-------------------------------------------
'''
Viết chương trình:
Khai báo 1 list gồm 5 phần tử số (nguyên và số thực). In ra kết quả
Khai báo 1 list gồm 3 phần tử: 1 string, 1 số và 1 list. In ra kết quả
'''
lst_1 = [1, 5, 6.5, 9.9, 88]
lst_2 = ['k', 159, [9, 7.5, 't']]
print(lst_1)
print(lst_2)

'''
Nhập vào 1 số nguyên dương n
- Khai báo list a gồm n phần tử 0, in ra a
- Khai báo list b gồm n phần tử 1 - n, in ra b
- Khai báo list c gồm n phần tử lẻ từ 1, 3, 5, ... in ra c
'''
n = int(input('Nhap n:'))
a = [0] * n
b = [1 - n] * n
c = []
for i in range(n):
    c.append(i * 2 + 1)
print('a = ', a)
print('b = ', b)
print('c', c)

'''
Nhập vào số nguyên dương n. Khai báo list a, nhập n phần tử vào list a.
Yêu cầu:
Khai báo list b và copy các giá trị của a vào b theo đúng thứ tự
Khai báo list c và copy các giá trị của a vào c theo chiều đảo ngược
'''
n = int(input('Nhap n:'))
a = []
for i in range(n):
    val = int(input(f'Nhap gia trithu {i}: '))
    a.append(val)
b = a.copy()
print('b = ', b)
c = []
for i in range(len(a)):     # len = 5
    indx = len(a) - i - 1   #indx = 5 - 0 -1
    c.append(a[indx])       # c.append(a[4]) = 5
print('c = ', c)

'''
Nhập vào số nguyên dương n. Nhập vào n phần tử cho list a. Tiếp theo,
nhập vào 2 số nguyên dương a, b sao cho 0 <= a <= b < n. Hỏi:
Phần tử từ ở vị trí a là gì
Phần tử từ vị trí a -> vị trí b là gì
In ra phần tử từ vị trí a -> vị trí b, mỗi 3 phần tử lấy ra và in 1 lần
'''
while True:
    n = int(input('Nhap n: '))
    a = int(input('Nhap a: '))
    b = int(input('Nhap b: '))
    if 0 < a < b < n:
        break
    else:
        print('Nhap sai. Nhap lai!')
lst = []
for i in range(n):
    val = int(input(f'Nhap gia trithu {i}: '))
    lst.append(val)
print('lst = ', lst)
print(lst[a:b])
print(lst[a:b:3])

'''
Nhập vào số n, nhập vào list n phần tử số thực. Hỏi:
Tổng các số trong list là bao nhiêu
Phần tử lớn nhất - nhỏ nhất có vị trí nào, giá trị bao nhiêu
'''
n = int(input('Nhap n = '))
lst = []
s = 0
for i in range(n):
    val = int(input(f'Nhap gia tri: '))
    lst.append(val)
max_val = lst[0]
min_val = lst[0]
for i in range(0, len(lst)):
    s += lst[i]
    if lst[i] < min_val:
        min_val = lst[i]
    if lst[i] > max_val:
        max_val = lst[i]
print(s)
print(lst.index(max_val))
print(lst.index(min_val))


'''
lst = [1, 6, 7, 22, 66, 99, 35, 46]
for i, v in enumerate(lst):
    print(i, v)

# tuong tu
for i in range(len(lst)):
    v = lst[i]
    print(i, v)

# list nguoc
for i, v in enumerate(lst[::-1]):
    print(i, v)
'''