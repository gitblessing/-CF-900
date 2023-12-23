inp = list(map(int,input().split()))
n,m = inp[0],inp[1]
left_socks = n
j = 0
day = 0

while left_socks>0:
    j+=1
    left_socks-=1
    
    if j%m==0:
        left_socks+=1
        day+=1
    else:
        day+=1
        continue
    
print(day)