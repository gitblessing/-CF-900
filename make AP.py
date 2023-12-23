# Failed Some Unknown TestCases rest fine


for no_testcase in range(int(input())):
    a,b,c = map(int,input().split())
    
    if (2*b)-a-c==0:
        print("YES")
        
    elif int(((2*b)-c)/a) == (((2*b)-c)/a) and (((2*b)-c)/a)>0:
        print("YES")
    elif int(((2*b)-a)/c) == (((2*b)-a)/c) and (((2*b)-a)/c)>0:
        print("YES")
    elif int((a+(abs(c-a))/(2))/b) == ((a+(abs(c-a))/(2))/b) and ((a+(abs(c-a))/(2))/b)>0:
        print("YES")
    else:
        print("NO")
         
  