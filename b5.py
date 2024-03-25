n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
x = int(input('Nhap x: '))

def dem(a, x):
    dem = 0
    for i in range(len(a)):
        if a[i] == x:
            a[i] = str(a[i]) + 'x'
            dem += 1
    print(a)
    print("So lan xuat hien cua", x, "la:", dem)

dem(a, x)
  
            
