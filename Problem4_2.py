#block1:
def input_new_numbers():
    inputs = []
    count = 1
    print("Number of input:")
    N = int(input())
    while count <= N:
        n = input()
        if len(n) != 4 :
            print("Please input again! Invalid number with {} digits".format(len(n)))
        elif "0" in n:
            print("Please input again! Invalid number")
        else:
            inputs.append(n)
            count += 1

    return inputs
inputs = input_new_numbers()


#block2:
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

process=[]

for number in inputs:
    a = number[0]
    b = number[1]
    c = number[2]
    d = number[3]
    label=cards(a,b,c,d)
    process.append(label)

for output in process:
    print(output)


