def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)
numbers = int(input("Enter an integer: "))

print(f"The Fibonacci sequence for {numbers} is:")
if numbers < 0:
    print("Please enter a positive integer")
else:
    for i in range(numbers):
        print(fibo(i), end=" ")
    print("\n")
