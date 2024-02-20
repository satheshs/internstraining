def solve(st):
    if st==st[::-1]:
        return "Given String is Palindrome"
    else:
        return "Given String is not a Palindrome"

st=input("Enter the String: ")
print(solve(st))