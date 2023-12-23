t = int(input())
inp = list(map(int,input().split()))
steps = 0
lis = []
minus_count = 0
zero_count = 0
for i in inp:
    diff = 0 
    if i==0:
        zero_count+=1
        lis.append(0)
    elif i ==1:
        lis.append(1)
    elif i==-1:
        lis.append(-1)
        minus_count+=1
    elif i>0 and i!=1:
        diff = i-1
        steps += diff
        lis.append(1)
    elif i<0 and i!= -1:
        diff = -1-i
        steps += diff
        lis.append(-1)
        minus_count+=1

if zero_count==0 and minus_count%2!=0:
    steps+=2
    
elif zero_count!=0 and minus_count%2==0:
    steps+=zero_count

elif minus_count%2!=0 :
    if zero_count!=0:
        zero_count-=1
        minus_count-=1
        steps+=1
    if zero_count!=0:
        steps+=zero_count
    
    

print(steps)