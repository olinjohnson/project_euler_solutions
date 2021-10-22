numNaturalNumbers = 100

def main():
    sumSquares = 0
    sumNums = 0
    for i in range(1, numNaturalNumbers + 1):
        sumSquares += i * i
        sumNums += i
    sumNums *= sumNums
    print("Difference between sum of squares and the square of the sum: ", sumNums - sumSquares)


if __name__ == "__main__":
    main()