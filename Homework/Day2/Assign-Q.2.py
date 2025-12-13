num = int(input("Enter a 5-digit number: "))
if 10000 <= num <= 99999:
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Please enter a valid 5-digit number.")