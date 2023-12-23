import math 
n = int(input())
lis = list(map(int,input().split()))
lis.sort()
total = 0
for i in lis:
    total+=i
j=0
t=0
while j<int(math.ceil(total/2)):
    j+=lis[t]
    t+=1
    
print(t+1)
