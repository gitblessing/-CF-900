import math
for no_testcase in range(int(input())):
    n = int(input())
    count = 0
    moves= 0
    while n%6==0:
        n=n/6
        count+=1
    if (math.log(n,3)).is_integer():
        moves = count + int(math.log(n,3)) 
    else:
         moves = -1
    print(moves)