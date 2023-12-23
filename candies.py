for testcases in range(int(input())):
    n = int(input())
    
    for j in range(1,n):
        for i in range(2,n):
            if ((2**j)-1)*i==n:
                print(j)
                break