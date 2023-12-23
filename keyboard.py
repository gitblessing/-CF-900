"""qwertyuiop
asdfghjkl;
zxcvbnm,./ """

l = ['q','w','e','r','t','y','u','i','o','p','next','a','s','d','f','g','h','j','k','l',';','next','z','x','c','v','b','n','m',',','.','/','last'] 

shift = input("")
inp_str = input("")
inp = [] 
res = []
for t in inp_str:
    inp.append(t)

if shift == "R":
    for i in inp_str:
        index = l.index(i)
        res.append(l[index-1])

if shift == "L":
    for i in inp_str:
        index = l.index(i)
        res.append(l[index+1])
print(*res,sep ="")