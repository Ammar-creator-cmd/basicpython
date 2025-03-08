"""#activity 1 : print the last digit of a number
n = int(input("Enter an integer: "))
last_digit = n % 10
print("The last digit of", n, "is", last_digit)
#activity 2 : print the 1st of the digits of a number
n = int(input("Enter an integer: "))
while n >=10:
    n = n // 10
print("The first digit ",n)

#palindromw seeker
def check_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit
        n = n // 10
    return original == reverse

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if check_palindrome(n):
        print(n, "is a palindrome")
    else:
        print(n, "is not a palindrome")"""

#activity 3 : denominatuion of a number
amount = int(input("Enter the amount: "))

num_100 = amount // 100
amount%=100

num_50 = amount // 50
amount%=50

num_10 = amount // 10
amount%=10

num_1= amount

print(f"100:{num_100}")
print(f"50:{num_50}")
print(f"10:{num_10}")
print(f"1:{num_1}")