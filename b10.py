n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
b = a.copy()
def sx_tang(a):
    a.sort()
    return a
def sx_giam(b):
    b.sort(reverse = True)
    return b
def xoa_tang(a, n):
    num = n
    mang = sx_tang(a)
    mang.pop(num-1)
    mang.pop(0)
    print(mang)
def xoa_giam(b, n):
    num = n
    mang = sx_giam(b)
    mang.pop(num-1)
    mang.pop(0)
    print(mang)
sx_tang(a)
sx_giam(b)
xoa_tang(a, n)
xoa_giam(b, n)
