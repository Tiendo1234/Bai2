n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def scp(a):
    dem_scp = 0
    mang_scp = []
    for i in a:
        for c in range(1, i+1):
            if(c*c == i):
                dem_scp+=1
        if(dem_scp == 1):
            mang_scp.append(i)
            dem_scp = 0
        else:
            dem_scp = 0
    return mang_scp
def chen(a):
    mang = []
    for i in scp(a):
        mang.append(i)
    for i in range(len(mang)):
        mang[i] = '0' + str(mang[i])
    return mang

# print(mang1)
print(scp(a))
print(chen(a))