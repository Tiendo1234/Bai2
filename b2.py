n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def sdx(a):
    sdx = 0
    mang = []
    mang1 = []
    for i in a:
        sdx = i%10
        a = i
        a //= 10
        if(sdx == a):
            mang.append(i)
        else:
            continue
    mang.sort()
    return mang
def not_sdx(a):
    arr_last = []
    for i in a:
        if(i not in sdx(a)):
            arr_last.append(i)
    arr_last.sort(reverse=True)
    return arr_last
def dem_sdx(a):
    dem = 0
    for i in a:
        if(i in sdx(a)):
            dem+=1
    return dem
print(sdx(a))
print(not_sdx(a))
print(dem_sdx(a))
        



