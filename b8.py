n = int(input('Nhập n: '))
def check_nt(n):
    dem=0
    arr = []
    for i in range(1, n+1):
        if(n%i==0):
            dem+=1
            arr.append(i)
    if(len(arr) == 0):
        arr = []
    else:
        return arr
def thua_so(n):
    thua_so = []
    dem = 0
    for i in check_nt(n):
        if(i == 1):
            continue
        for a in range(1, i+1):
            if(i%a==0):
                dem+=1
        if(dem==2):
            dem = 0
            thua_so.append(i)
        else:
            continue
    return tuple(thua_so)
check_nt(n)
print(thua_so(n))

