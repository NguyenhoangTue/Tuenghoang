print('問題6(Cランク):給与の計算')
print('URL:https://paiza.jp/challenges/365/show')
print("________________________________________")
#block1:input
n=[]
for x in range(1):
  salary_per_hours = input().rstrip().split(' ')
  #print(salary_per_hours)
working_days = int(input())
for i in range(working_days):
  working_time = input().rstrip().split(' ')
  print(working_time)
  started_time = working_time[0]
  ended_time = working_time[1]
  print(started_time)
  print(ended_time)










