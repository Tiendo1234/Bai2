n = int(input('Nhap n: '))
a = [int(input('Nhap phan tu: ')) for i in range(n)]
duong = []
am = []
def dem(a):
    dem = 0
    dem1 = 0
    dem_duong = 0
    dem_am = 0
    # tbc_duong = 0.0
    # tbc_am = 0.0
    for i in a:
        if(i > 0 == 0):
            dem+=1
            dem_duong+=i
            duong.append(i)
        else: 
            dem1+=1
            dem_am+=i
            am.append(i)
    tbc_duong = float(dem_duong/dem)
    tbc_am = float(dem_am/dem1)
    print('So duong co trong list la: ', dem)
    print('So am co trong list la: ', dem1)
    print('Trung binh cong cac so duong: ', tbc_duong)
    print('Trung binh cong cac so am: ', tbc_am)
dem(a)