print('問題5(Cランク):試験の合格判定')
print('URL:https://paiza.jp/challenges/153/show')
print("________________________________________")
#block1:input
N=int(input())
n=[]
pass_number=0
input_line = N
for i in range(input_line):
  x = input().rstrip().split(' ')
  n.append(x)
#block 2: dieukien(s) = True/False
pass_list=[]
for m in n:
  x=m
  total= int(x[1])+ int(x[2]) + int(x[3]) + int(x[4]) + int(x[5])

  total_rikei= int(x[2]) + int(x[3])

  total_bunkei= int(x[4]) + int(x[5])

  if x[0] == "l":
    if (total >= 350) and (total_bunkei >= 160):
      pass_list.append("PASSED")
    else:
      pass_list.append("FAILED")
  elif x[0] == "s":
    if (total >= 350) and (total_rikei >= 160):
      pass_list.append("PASSED")
    else:
      pass_list.append("FAILED")

for sth in pass_list:
  print(sth)


