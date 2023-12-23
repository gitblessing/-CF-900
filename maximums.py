n = int(input())
b = list(map(int,input().split()))
b.insert(0,0)

x = []
for i in range(1,n+1):
    temp = b[:i]
    print(temp)
    # xi = max(temp)
    # x.append(xi)
#print(x)