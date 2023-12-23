import math 
for no_testcase in range(int(input())):
    a,b,c,d = map(int,input().split())
    taken = b
    left = a-b
    if b>=a:
        taken = b
    
    elif c-d<=0:
        taken = -1
    
    else:
        taken += math.ceil(left/(c-d))*c
        
    print(taken)