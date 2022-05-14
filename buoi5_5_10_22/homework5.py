#github: https://github.com/imharunguyen/python-core

#----Tìm max min và vị trí
n = int(input('n = '))
min_val, max_val = 0, 0
min_val_ind, max_val_ind = 0, 0

for i in range(n):
    temp = int(input())
    if i:
        if temp < min_val:
            min_val = temp
            min_val_ind = i
        if temp > max_val:
            max_val = temp
            max_val_ind = i
    else:
        min_val = temp
        min_val_ind = i

        max_val = temp
        max_val_ind = i

print('Min:', min_val, 'o vi tri', min_val_ind)
print('Max:', max_val, 'o vi tri', max_val_ind)

#-------------tổng các số, số lẻ
n = int(input('n = '))
even_sum = 0
even_sum_str = ''
odd_sum = 0
odd_sum_str = ''

for i in range(n):
    temp = int(input())
    if temp % 2 == 0:
        even_sum += temp
        if even_sum_str != '':
            even_sum_str += ' + '
        even_sum_str = f'{even_sum_str}{temp}'
    else:
        odd_sum += temp
        if odd_sum_str != '':
            odd_sum_str += ' + '
        odd_sum_str = f'{odd_sum_str}{temp}'

print(odd_sum_str, '=', odd_sum)
print(even_sum_str, '=', even_sum)
