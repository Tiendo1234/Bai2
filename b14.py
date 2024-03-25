n = int(input('Nhap n: '))
arr = [int(input('Nhap phan tu: ')) for i in range(n)]
def to_hop(arr):
    mang = []
    for a in range(1, max(arr)+1):
        for b in range(1, max(arr)+1):
            for c in range(1, max(arr)+1):
                if(a > abs(b-c)) and (a > abs(b+c)) or a > b and a > c:
                    mang.append([a, b, c])
    return mang
print(to_hop(arr))