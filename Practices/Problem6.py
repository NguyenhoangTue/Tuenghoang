# Step 1:
# Tinh luong 1 ngay theo so da nhap
def tinhluong_one_day(start_time, end_time):
  # tinh luong cua tung gio

  # Tao list gom cac phan tu co gia tri >= start_time, < end_time
  # vi du
  # start_time = 9, end_time = 11 - > list = [9, 10]
  # start_time = 22, end_time = 5 - > list = [22, 23, 0, 1, 2, 3, 4]
  # list nay minh muon lay ten là list_time

  list_time = []
  if start_time < end_time:
    # start_time = 9, end_time = 11 - > list = [9, 10]
    for i in range(end_time - start_time): # range(2) -> [0 , 1]
      list_time.append(start_time + i)
  else:
    # start_time = 22, end_time = 5 - > list = [22, 23, 0, 1, 2, 3, 4]
    for i in range(end_time + 24 - start_time): # 29 - 22 = 7 -> [0, 1, 2, 3, 4, 5, 6]
      if start_time + i < 24: # start_time = 22 -> 0, 1
        list_time.append(start_time + i)
      else: # i = 2, 3, 4, 5, 6, start_time = 22
        list_time.append(start_time + i - 24)

  # tinh tong tien
  total = 0

  for hour in list_time: # [22, 23, 0, 1, 2, 3, 4]
    if 0 <= hour < 9:
      total = total + int(salary_per_hours[2])
    elif 9 <= hour < 17:
      total = total + int(salary_per_hours[0])
    elif 17 <= hour < 22:
      total = total + int(salary_per_hours[1])
    else:
      total = total + int(salary_per_hours[2])

  return total

# print('問題6(Cランク):給与の計算')
# print('URL:https://paiza.jp/challenges/365/show')
# print("________________________________________")
# #block1:input
# n=[]
# Nhap so tien luong tinh theo gio
for x in range(1):
  salary_per_hours = input().rstrip().split(' ')

# Nhap so gio lam tung ngay
working_days = int(input())
tong_luong = 0
for i in range(working_days):
  working_time = input().rstrip().split(' ')
  started_time = working_time[0]
  ended_time = working_time[1]

  # luong 1 ngay
  luong_1_ngay = tinhluong_one_day(int(started_time), int(ended_time))
  tong_luong = tong_luong + luong_1_ngay

print('{}'.format(tong_luong))

# Xu ly: tính luong theo so ngay da nhap




# Step 2:
# Tinh luong theo so ngày da nhap













