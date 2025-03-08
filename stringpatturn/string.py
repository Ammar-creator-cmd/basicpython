n = int(input("enter number of rows: "))
for i in range(1, n+1):
    print("*"*i)
# The above code is to print a pattern of stars in the form of a right triangle.

n = int(input("enter number of rows: "))
for i in range(1, n+1):
    spaces = ""*(n-i)   
    asterisks = "* "*i
    print(spaces + asterisks)

for unicode in range(65,91):
    print(chr(unicode)) # changes the unicode to character

#substring builder
name = input("enter a string: ")
for i in range(1, len(name) + 1):
    substring = name[:i]
    spacedSubstring = " ".join(substring)
    print(spacedSubstring) # prints a triangle of the string
#alphabet ascender
n = int(input("enter number of rows: "))
startUnicode = 65 # (ASCII)unicode for A
for i in range(1, n+1):
    for j in range(i):
        lettr = chr(startUnicode)
        print(lettr, end=" ")
        startUnicode += 1
    print()