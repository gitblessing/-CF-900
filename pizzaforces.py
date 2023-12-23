for testcases in range(int(input())):
    n = int(input())
    mins  = 2.5*n
    if mins<=15:
        ans = 15
    
    elif mins.is_integer():
        t = mins%5
        if  t==0:
            ans = mins
        else:
            ans = mins+ 5-t
    else:
        mins+=0.5
        t = mins%5
        if  t==0:
            ans = mins
        else:
            ans = mins+ 5-t
    print(int(ans))
