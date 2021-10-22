def main():
    # Beware: probably not the most efficient code
    for a in range(1, 999):
        for b in range(1, 999):
            for c in range(1, 999):
                    if a + b + c == 1000:
                        if a < b and b < c:
                            if a*a + b*b == c*c:
                                print("Pythagorean Triplet: ", a, " ", b, " ", c, " Product: ", a*b*c)
                                return

if __name__ == "__main__":
    main()