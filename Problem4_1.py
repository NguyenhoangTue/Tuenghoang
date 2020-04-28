def cards(a, b, c, d):
    if a == b == c == d:
        return"Four Cards"
    elif a == b == c or b == c == d or a == c == d:
        return "Three Cards"
    elif a == b and c == d:
        return 'Two Pairs'
    elif a == b or c == d or b == c:
        return "One Pair"
    else:
        return "No Pair"

n=1
N=int(input("Numbers: "))
answer = []
while n <= N:
    raw = int(input())
    if len(str(raw)) <= 4:
        a = int(raw / 1000)
        b = int((raw - a * 1000) / 100)
        c = int((raw - a * 1000 - b * 100) / 10)
        d = int((raw - a * 1000 - b * 100 - c * 10))
        label = cards(a,b,c,d)
        answer.append(label)
        n = n + 1
    else:
        print("Error")
for ans in answer:
    print(ans)


