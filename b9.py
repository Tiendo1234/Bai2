x = int(input('Nhap x: '))
y = int(input('Nhap y: '))
def so(x,y):
    mang = []
    for i in range(x+1, y):
        if(i % 2 == 0) and (i % 3 == 0):
            mang.append(i)
    return tuple(mang)
print(so(x, y))