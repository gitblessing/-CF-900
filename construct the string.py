for testcases in range(int(input())):
    n,a,b = map(int,input().split())
    ans =[]
    for i in range(b):
        ans.append(chr(97+i))
    print(*ans*(n//b),*ans[0:n%(n//b)-1], sep = "")
