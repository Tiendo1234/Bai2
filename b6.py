n = int(input('n: '))
a = [input('Nhap chu: ') for i in range(n)]
def chu(a):
    for i in range(len(a)):
        a[i] = a[i].upper()
    return tuple(a)
print(chu(a))
