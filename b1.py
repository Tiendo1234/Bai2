n = int(input('Nhap n: '))
a = [int(input()) for i in range(n)]

def snt(a):
    dem_snt = 0
    mang_snt = []
    for i in a:
        for b in range(1, i+1):
            if(i % b == 0):
                dem_snt += 1
        if(dem_snt == 2):
            mang_snt.append(i)
            dem_snt = 0
        else:
            dem_snt = 0
    return mang_snt
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
def non_snt_scp(a):
    mang_conlai = []
    for e in a:
        if (e not in snt(a)) and (e not in scp(a)):
            mang_conlai.append(e)
    return mang_conlai
print(tuple(snt(a)))
print(tuple(scp(a)))
print(tuple(non_snt_scp(a)))