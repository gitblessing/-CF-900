n,k = map(int,input().split())
peace = 0
maxp = -9000000000000000000000000000000
for i in range (n):
    f,t = map(int,input().split())
    if k>t:
        peace = f
    else:
        peace = f-t+k
    
    if peace>maxp:
        maxp = peace
print(maxp)
        