a = int(input("enter a whole number "))
b = []
for i in range(a):
    c = input(" ")
    b.append(c)
print("Original list", b)
b[0], b[-1] = b[-1], b[0]
print("Swapped list", b)
