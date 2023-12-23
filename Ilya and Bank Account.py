num = int(input())
zero =["-","-0","0"]
if num>=0:
    print(num)
else:
    string = str(num)
    l_str = string[:-1]
    l2_str = string[:-2] + string[-1]
    if l_str in zero or l2_str in zero:
        print("0")
    elif l_str < l2_str:
        print(l_str)
    else:
        print(l2_str)
    
   
    
    
    

    