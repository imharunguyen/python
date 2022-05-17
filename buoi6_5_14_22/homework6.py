

#---số đối xứng
n = int(input('n = '))
temp = n
n_sodoi = 0
while temp != 0:
    x = temp % 10
    n_sodoi = n_sodoi * 10 + x
    temp //= 10

if n_sodoi == n:
    print('la so doi xung')
else:
    print('khong la so doi xung')

