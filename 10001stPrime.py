import math

def main():
    num = 10001
    counter = 1
    prime = 1
    while(counter < num):
        n = prime
        while(True):
            n += 1
            if isNumberPrime(n):
                prime = n
                break
        counter += 1
    
    print("10,001st prime: ", prime)

def isNumberPrime(num):
    for i in range(2, max(math.ceil(num / 2), 3)):
        if num % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    main()