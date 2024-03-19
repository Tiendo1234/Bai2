n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def sdx(a):
    sdx = 0
    mang = []
    mang1 = []
    for i in a:
        sdx = 0*10 + i%10
        i // 10
        if(sdx == i):
            mang.append(i)
        else:
            mang1.append(i)
    mang.sort(reverse=True)
    mang1.sort()
    return mang1, mang
print(sdx(a))
        



