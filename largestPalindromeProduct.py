import math

def main():
    highestProduct = 0
    for i in range(1000, 100, -1):
        for x in range(1000, 100, -1):
            product = str(i * x)
            n = math.floor(len(product) / 2)
            c = 0
            for z in range(1, n + 1):
                if product[z - 1] == product[-z]:
                    c += 1

            if c == n and int(product) > highestProduct:
                highestProduct = int(product)
                
    print("Highest palindrome of 3 digit factors: ", highestProduct)


if __name__ == "__main__":
    main()