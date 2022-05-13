#github: https://github.com/imharunguyen/python-core

#----Tìm max min và vị trí
n = int(input('Nhap so so muon nhap: '))
M = 0
m = 0
for i in range(n):
    x = int(input())
    if x > M:
        M = x
        locate_M = i
    if x < m:
        m = x
        locate_m = i

print('Min:', m, 'o v tri', locate_m)
print('Max:', M, 'o vi tri', locate_M)

#-------------tổng các số, số lẻ
n = int(input('Nhap so so muon nhap: '))
s_all = 0
s_odd = 0
all = ''
odd = ''
for i in range(n):
    x = int(input())
    s_all += x
    all += str(x) + ' + '
    if x % 2 != 0:
        odd += str(x) + ' + '
        s_odd += x
print('Tong cac so la:    ', all, '=', s_all)
print('Tong cac so le la: ', odd, '=', s_odd)

