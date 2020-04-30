for i in range(1):
    so_ngay_nghi_va_so_ngay_di_choi = input().rstrip().split(' ')
    so_ngay_nghi = int(so_ngay_nghi_va_so_ngay_di_choi[0])
    so_ngay_di_choi = int(so_ngay_nghi_va_so_ngay_di_choi[1])
    list_luong_mua=[]
    list_holiday=[]
    for x in range(so_ngay_nghi):
        day_va_luong_mua=input().rstrip().split(' ')
        list_luong_mua.append(int(day_va_luong_mua[1]))
        list_holiday.append(int(day_va_luong_mua[0]))
    print(list_holiday)
    print(list_luong_mua)


#Muc tieu tinh trung binh cong luong mua cua n ngay di choi trong N ngay nghi
#Vi du, nghi 7 ngay, di choi 3 ngay
#Dang co list_holiday [19,20,21,22,23,24,25] va list_luongmua[0,0,60,30,10,10,90]
#step1
list_luong_mua = [0,0,60,30,10,10,90]
so_ngay_di_choi = 3

z=0
for z in range(len(list_luong_mua)):#range(7) (0,1,2,3,4,5,6)
    list_luong_mua_n_ngay_di_choi=[]
    for y in range(so_ngay_di_choi): #range(3) (0,1,2)











