import math

def main():
    sum = 0
    for i in range(1, 2000000):
        if isNumberPrime(i):
            sum += i

    print("Sum of all prime numbers below 2,000,000: ", sum)

def isNumberPrime(num):
    
    for i in range(2, math.ceil(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    print("PRIME: ", num)
    return True

if __name__ == "__main__":
    main()