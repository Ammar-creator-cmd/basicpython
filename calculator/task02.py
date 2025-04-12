n = int(input("enter a number to create a multiplication table: "))
row = int(input("enter a number for n to be multiplied to: "))
for i in range(1, row+1):
    print(f"{n} x {i} = {n*i}")

