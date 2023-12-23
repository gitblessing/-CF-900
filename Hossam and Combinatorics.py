for no_testcase in range(int(input())):
    n = int(input())
    l = sorted(map(int,input().split()))
    if len(set(l))==1 and n%2==0:
        print(int((n/2)*(n/2)*2))
        
    elif len(set(l))==1 and n%2!=0:
        print(int(((n-1)/2)*((n+1)/2)*2))
        
    else:
        c_min,c_max=l.count(l[0]),l.count(l[-1])
        print(c_min*c_max*2)