for testcases in range(int(input())):
    n = int(input())
    ans = "NO"
    if n%2==0:
        ans = 'NO' 
    else:
        if n==3:
            ans = "YES"
        else:
            for i in range(3,n,2):
                if n%i==0:
                    ans = "YES"
                    break
                else:
                    continue
                    
    print(ans)