n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def tim_max(a):
    so_max = a[0]
    so_lon = []
    for i in a:
        if(i > so_max): 
            so_max = i
        else: 
            if(i == so_max):
                a.remove(i)
    print(so_max)
    print('List con lai: ', a)
tim_max(a)