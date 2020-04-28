def cards(a, b, c, d):
    if a == b == c == d:
        answers.append("Four Cards")
    elif a == b == c or b == c == d or a == c == d:
        print("Three Cards")
    elif a == b and c == d:
        print('Two Pairs')
    elif a == b or c == d or b == c:
        print("One Pair")
    else:
        print("No Pair")


def answer(answers):
    pass

# Input(number)  -> process -> evaluate("which type") -> loop
# Paiza: N(number of input) + input(list of numbers-with-four-digit)
# Output: list of string ("One pair, two pair, three cards, ..")
# Before use list, initialize list
# from
class Problem4(object):
    def __init__(self):
        pass
# to: nothing
    # public
    # Split into blocks
    def input_new_numbers():
        inputs = []
        count = 1
        print("Number of input:")
        N = int(input())
        # Loop N times
        while count <= N:
            # Check for valid input
            print("4-digit-numbers:")
            n = int(input())
            if len(str(n)) != 4:
                print("Please input again! Invalid number with {} digits".format(len(str(n))))
                print("4-digit-numbers:")
                n = int(input())
            else:
                # Create list to save 4-digits number
                inputs.append(n)
                count += 1

        # Only run when while loop end
        return inputs

    def processing(self):
        pass
    def output(self):
        pass

# Entry point
# def main():
if __name__ ==  "__main__":
    count = input_new_numbers()
    print(count)

    # Processing

    # Answer

"""
while n<=N:
    # Input (number)
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

"""
