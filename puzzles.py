inp = list(map(int,input().split()))
n,m = inp[0],inp[1]
inp2 = list(map(int,input().split()))

inp2.sort(reverse = False)

i=0
min = inp2[n-1] - inp2[0] 
for j in range (m+1-n):
    if inp2[j+n-1] - inp2[j] < min:
        min = inp2[j+n-1] -inp2[j]
        j+=1
    else:
        j+=1
print(min)
