def input_new_numbers():
    # make a list
    inputs = []
    # make count
    count = 1
    print("Number of input:")
    N = int(input())
    # Loop N times
    while count <= N:
        # Check for valid input
        #n la so nhap vao
        n = int(input())
        if len(str(n)) != 4:
            print("Please input again! Invalid number with {} digits".format(len(str(n))))

            n = int(input())
        else:
            # Create list to save 4-digits number
            inputs.append(n)
            count += 1
        #

    # Only run when while loop end
    return inputs
inputs = input_new_numbers()
print(inputs)
#Example:N=2 n=2222,4455
#inputs= [2222,4455]
for cards in inputs:
    for process in range(cards):
        def output(a, b, c, d):
            if a == b == c == d:
                print("Four Cards")
            elif a == b == c or b == c == d or a == c == d:
                print("Three Cards")
            elif a == b and c == d:
                print('Two Pairs')
            elif a == b or c == d or b == c:
                print("One Pair")
            else:
                print("No Pair")















