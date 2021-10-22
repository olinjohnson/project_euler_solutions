def main():
    num1 = 0
    num2 = 1
    sum = 0
    while(num2 <= 4000000):
        if num2 % 2 == 0:
            sum += num2
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print("Sum of even Fibonacci numbers: ", sum)

if __name__ == "__main__":
    main()