N=int(input("Numbers:"))
n=1

def cards(a, b, c, d):
    if a == b == c == d:
        print("Four Cards")
    elif a == b == c or b == c == d or a == c == d:
        print("Three Cards")
    elif a == b and c == d:
        print('Two Pairs')
    elif a == b or c == d or b==c :
        print("One Pair")
    else:
        print("No Pair")

while n<=N:
    raw = int(input())
    if len(str(raw))<=4 :
        a = int(raw / 1000)
        b = int((raw - a * 1000) / 100)
        c = int((raw - a * 1000 - b * 100) / 10)
        d = int((raw - a * 1000 - b * 100 - c * 10))
        cards(a, b, c, d)
        n = n + 1
    else:
        print("Error")

