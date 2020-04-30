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
    # print(list_holiday)
    # print(list_luong_mua)

# Tìm N ngày có lượng mua trung bình nhỏ nhất
# Tìm lượng mua trung bình của N(3) ngày

def tinh_luong_trung_binh(start_index_of_list_holiday, N):

    # start_index_of_list_holiday = 0 (ngày 22) , N= 3
    total_luong_mua = 0
    for i in range(N): # i = [0, 1, 2]
        total_luong_mua = total_luong_mua + list_luong_mua[i + start_index_of_list_holiday]

    average_luong_mua = total_luong_mua / N
    
    return average_luong_mua

#print(tinh_luong_trung_binh(1, 3))

def tao_list_luong_mua_trung_binh(N):
    # N = 3
    list_luong_mua_trung_binh = []
    for i in range(len(list_luong_mua) - N + 1): # i = [0, 1]
        luong_mua_tb = tinh_luong_trung_binh(i, N)
        list_luong_mua_trung_binh.append(luong_mua_tb)
        
    return list_luong_mua_trung_binh

def tim_index_luong_mua_trung_binh_nho_nhat(list_luong_mua_tb):
    min_index = 0
    min_luong_mua_trung_binh = list_luong_mua_tb[0] # 20
    for i in range(len(list_luong_mua_tb)):
        if list_luong_mua_tb[i] < min_luong_mua_trung_binh:
            min_luong_mua_trung_binh = list_luong_mua_tb[i]
            min_index = i

    return min_index


list_luong_mua_tb = tao_list_luong_mua_trung_binh(3)
min_index = tim_index_luong_mua_trung_binh_nho_nhat(list_luong_mua_tb)
# print(min_index)
print('{} {}'.format(list_holiday[min_index], list_holiday[min_index + so_ngay_di_choi - 1], ))

#Muc tieu tinh trung binh cong luong mua cua n ngay di choi trong N ngay nghi
#Vi du, nghi 7 ngay, di choi 3 ngay
#Dang co list_holiday [19,20,21,22,23,24,25] va list_luongmua[0,0,60,30,10,10,90]
#step1
# list_luong_mua = [0,0,60,30,10,10,90]
# so_ngay_di_choi = 3
#
# z=0
# for z in range(len(list_luong_mua)):#range(7) (0,1,2,3,4,5,6)
#     list_luong_mua_n_ngay_di_choi=[]
#     for y in range(so_ngay_di_choi): #range(3) (0,1,2)
#         pass












