def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def fibonacci_sequence(n):
    num1 = 0
    num2 = 1

    print("Fibonacci sequence:")
    print(num1)
    print(num2)

    for i in range(2, n):
        next_num = num1 + num2
        print(next_num)
        num1 = num2
        num2 = next_num

def pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print ascending numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print descending numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        # Move to the next line
        print()

if __name__ == "__main__":
    table(2)
    print()
    number_triangle(5)
    print()
    fibonacci_sequence(10)
    print()
    pyramid(5)

