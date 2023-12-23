inp = list(map(int,input().split()))
n,m = inp[0],inp[1]
max = 0
if n>m:
    max = n
    min = m
else:
    max = m
    min = n

if min%2==0:
    print("Malvika")
else:
    print("Akshat")