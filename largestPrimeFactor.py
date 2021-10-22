import math

primeFactorNum = 600851475143
def main():
    n = int(round(primeFactorNum / 2, 0))
    highestPrimeFactor = None
    for i in range(2, n):
        if primeFactorNum % i == 0:
            if isNumberPrime(primeFactorNum / i):
                highestPrimeFactor = primeFactorNum / i
                break
    print("Highest prime factor of 600851475143: ", highestPrimeFactor)

def isNumberPrime(num):
    for i in range(2, max(math.ceil(num / 2), 3)):
        if num % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    main()