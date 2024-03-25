n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def tim_max(a):
    lon = 0
    for i in a:
        if(i > lon):
            lon = i
        elif(i == lon):
            a.remove(i)
        else:
            continue
    print(lon)
    print('mang con lai: ', a)
tim_max(a)
