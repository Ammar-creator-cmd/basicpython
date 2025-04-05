def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

if __name__ == "__main__":
        n = int(input("Enter an integer: "))
        if n > 0 and n < 27:
            print_pattern(n)
        else:
            print("Invalid ineteger or out of range (1-26)")