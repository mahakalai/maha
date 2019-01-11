n=int(input())
c=0
if n<=100000000000:
    while n:
        rem=n%10
        c=c+1
        n=n//10
    print(c)
