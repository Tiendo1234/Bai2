n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
def duong(a):
    duong = []
    am = []
    for i in a:
        if(i%2==0):
            duong.append(i)
        else:
            am.append(i)  
    print(duong)
    print(am)
duong(a)