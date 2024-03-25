n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def uoc_max(a):
    mang = []
    dem = 0
    for i in a:
        for b in range(1, min(a) + 1):
            if(i % b == 0):
                dem+=1
        if(dem==2):
            mang.append(1)
            dem=0
            break
        else: 
            mang.append(b)
            
    return max(mang)
def scn_max(a):
    e = max(a)
    scn = []
    for i in a:
        if(i==e):
            continue
        else:
            scn.append(i)
    scn.sort(reverse=True)
    return scn[0]
def boi_min(a):
    boi = []
    dem1 = 0
    for i in a:
        for c in range(1, (max(a)*scn_max(a))+1):
            if(c*i == max(a)*scn_max(a)):
                dem1+=1
                boi.append(c)
        if(dem1==1):
            dem1=0
        else:
            boi.clear()
            break
    if(boi == []):
        return []
    else:
        return max(boi)
def dem(a):
    b = max(a)
    n = len(a)
    dem = 0
    for i in a:
        if(b%i==0):
            dem+=1
    if(dem==n):
        return max(a)
    else:
        return boi_min(a)
print(uoc_max(a))
print(scn_max(a))
print(dem(a))