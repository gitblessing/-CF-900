
def check_01(ch):
    if '01' in st:
        st.replace('01','')
        ch+=1
    
def check_10(ch):
    if '10' in st:
        st.replace('10','')
        ch+=1


for testcases in range(int(input())):
    st = str(input())
    ch =0 
    t = len(st)
    for i in range(t):
        check_01(ch)
        check_10(ch)

    if ch%2==0:
        print("NET",ch)
    else:
        print("DA",ch)