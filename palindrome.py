arr=str(input("Enter any String: "))
arr = arr.casefold()
if arr == arr[::-1]:
    print('Its a palindrome')
else:
    print('not a palindrome')
