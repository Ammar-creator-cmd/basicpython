def print_multiplication_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{i * j:4}", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    print_multiplication_triangle(n)
