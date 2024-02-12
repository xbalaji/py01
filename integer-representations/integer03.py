#! /usr/local/bin/python3

import math
import sys

def represent(n):
    representations = []
    for a in range(2, int(math.sqrt(n)) + 1):
        for b in range(1, int(math.log(n, a)) + 1):
            c = n - a ** b
            if c >= 0 and c < 9:
                representations.append((a, b, c))
    representations.sort(key=lambda x: x[1])
    for r in representations:
        print(f"{n} = {r[0]}^{r[1]} + {r[2]}")
    if representations:
        print(f"Selected representation: {n} = {representations[0][0]}^{representations[0][1]} + {representations[0][2]}")
    else:
        print(f"No representation found for {n}")

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("Please enter a positive integer: "))
    represent(n)

if __name__ == "__main__":
    main()


