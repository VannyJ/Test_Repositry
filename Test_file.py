pick = int(input("Please enter a value"))
def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    return 0

def guessNumber(n):
    for i in range(1, n):
        if guess(i) == 0:
            return i
        
def main():
    n = 15
    answer = guessNumber(n)

    print("The guessed nunber is ", answer)

main()