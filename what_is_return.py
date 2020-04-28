def my_function(input):
    if input > 10:
        return 10
    else:
        print(9)
        return 8
        print("end")
n = 0
while n<10:
    returns = my_function(n)
    print(returns)
    print("n", n)
    n += 1
