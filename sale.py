inp = list(map(int,input().split()))
n,m = inp[0],inp[1]
inp2 = list(map(int,input().split()))
inp2 = sorted(inp2)
sum = 0 
for i in range(m):
    if inp2[i]<0:
        sum = sum + inp2[i]


print(-sum)
    

