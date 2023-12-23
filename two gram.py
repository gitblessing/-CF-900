x = int(input())
str = input()
list1 = []
list2 = []
lis= []
for i in str:
    list1.append(i)
    list2.append(i)

for j in range (len(str)-1):
    two_gram = str[j] + str[j+1]
    lis.append(two_gram)


    
def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(lis))