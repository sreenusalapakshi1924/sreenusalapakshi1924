def age(n):
    if (n==0):
       return 'you are not born yet'
    elif (n==100):
        return 'your age is 100 years'
    else:
        x=100-n
        return x,'years needed to complete 100 years'
n=int(input('enter n value:'))
ag=age(n)
print(ag)

