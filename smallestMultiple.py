num = 20

def main():
    counter = num
    while(True):
        flag = 0
        for i in range(1, num + 1):
            if counter % i != 0:
                counter += num
                flag = 1
                break
                
        if flag == 1: 
            continue

        break

    print("Smallest multiple that can be divided by each number from 1 to ", num, ": ", counter)

if __name__ == "__main__":
    main()