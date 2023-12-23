for no_testcase in range(int(input())):
    n = input()
    inp = list(map(int,input().split()))
    
    inp.sort()
    maxi =inp[-1]
    # for i in range(maxi):
    #     for t in range(maxi):
    #         if inp[t]-inp[i]>0 and inp[t]-inp[i] not in inp:
    #             inp.append(inp[t]-inp[i])
                
    for i in range(maxi-1):
        for a in range(maxi-):
            if inp[-1-i]-inp[a]>0 and inp[-1-i]-inp[a] not in inp:
                inp.append(inp[-1-i]-inp[a])
                inp.sort()    
        
    print(len(inp))
    inp.sort()
    print(*inp)
   