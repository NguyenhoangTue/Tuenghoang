#Input:
#Paiza RankC C075 
list_so_tien_1_lan = []
for x in range(1):
    so_tien_ban_dau_va_so_lan_di_xe = input().rstrip().split(' ')
    for i in range(int(so_tien_ban_dau_va_so_lan_di_xe[1])):
        so_tien_1_lan=int(input())
        list_so_tien_1_lan.append(so_tien_1_lan)


    point=0
    tien_thua_sau_1_lan=int(so_tien_ban_dau_va_so_lan_di_xe[0])
    for tien_di_xe in list_so_tien_1_lan:
        if point < int(tien_di_xe):
           point = point + int(tien_di_xe)/10
           tien_thua_sau_1_lan -= int(tien_di_xe)
        else:
           point= point - int(tien_di_xe)

        #tien_thua=int(so_tien_ban_dau_va_so_lan_di_xe[0])-int(tien_di_xe)
        #tien_thua_sau_1_lan -= int(tien_di_xe)

        print(f"{tien_thua_sau_1_lan} {int(point)}")








