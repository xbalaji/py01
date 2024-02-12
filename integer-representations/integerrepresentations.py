#! /usr/local/bin/python3


def find_representations(n):
    representations = []

    for a in range(2, n):
        for b in range(2, n):
            c = n - a**b
            if 0 <= c < 9:
                representations.append((a, b, c))

    # Sort representations based on the value of 'b'
    representations.sort(key=lambda x: x[1])

    return representations


def main():
    try:
        n = int(input("Enter a positive integer n: "))
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        
        result = find_representations(n)

        if not result:
            print(f"There are no representations for {n}.")
        else:
            print(f"Representations for {n}:")
            for a, b, c in result:
                print(f"{a}^{b} + {c}  (Selected)" if (a, b, c) == result[0] else f"{a}^{b} + {c}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

