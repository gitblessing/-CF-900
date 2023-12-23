n,b,d = map(int,input().split())
inp = list(map(int,input().split()))
remain = d
empty_count = 0
for i in inp:
    if i>b:
        continue
    else:
        remain-=i
        
    if remain<0:
        empty_count+=1
        remain = d
print(empty_count)        
    