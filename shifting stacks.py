n=int(input())
for i in range(n):
    t = int(input())
    inp =list(map(int,input().split()))
    
    for j in range (t-1):
        if inp[j]==0:
            continue
        if inp[j]>=inp[j+1]:
            inp[j]-=1
            inp[j+1] +=1
        else:
            continue
    print(*inp)
    l=0
    for b in range(t-1):
        if inp[b]<inp[b+1]:
            continue
            
        else:
            l=1
    if l==1:
        print("NO")
    else:
        print("YES")
            
    