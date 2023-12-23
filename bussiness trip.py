
n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse = True)
x =0
ct = 0

if sum(arr)<n:
    print(-1)
else:
    for i in arr:
        
        if x>=n:
            break 
        else:
            x+=i
            ct+=1
    print(ct)