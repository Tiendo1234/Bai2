nt = []
cp = []
last = []
n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
so_cuoi = 0
def snt(a):
    dem = 0
    for i in a:
        if(a[n-1]%i==0):
            dem+=1
            nt.append(i)
    if(dem == 2):
        dem == 0
    if(dem > 2):
        dem = 0
        print('Khong phai so nguyen to')
    snt_1 = tuple(nt)
    return snt_1
def scp(a):
    dem_cp = 0
    for i in a:
        if(i*i == a[n-1]):
            dem_cp+=1
            cp.append(i)
    if(dem_cp == 0):
        print('Day la so chinh phuong')
    else:
        dem_cp = 0
        print('Day khong la so chinh phuong')
    scp_1 = tuple(cp)
    return scp_1
print(snt(a))
print(scp(a))

