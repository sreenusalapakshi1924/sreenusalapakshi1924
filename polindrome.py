def polindrome(N):
    if(N==N[::-1]):
        return 'given number is polindrome'
    else:
        return 'given number is not a polindrome'
N=input()
print(polindrome(N))