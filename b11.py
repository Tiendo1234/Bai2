n = int(input('Nhap so nguyen duong: '))
def so(n):
    x = 1/3
    mang = []
    for i in range(n+1):
        can_ba = i**x
        if(can_ba.is_integer()):
            mang.append(i)
    return tuple(mang)
print(so(n))