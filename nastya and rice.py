t = int(input(""))
while t>0:
    t-=1
    inp = list(map(int,input().split()))
    n,a,b,c,d = inp[0],inp[1],inp[2],inp[3],inp[4]
    
    max_total = c+d
    min_total = c-d
    max_individual = a+b
    min_individual = a-b
    
    if n*max_individual>=min_total and n*max_individual<=max_total:
        print("Yes")
    elif n*min_individual>=min_total and n*min_individual<=max_total:
        print("Yes")
    elif min_total==max_total:
        if (min_total>=(n*min_individual) and max_total<=(n*max_individual)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")