
import re
str = input()
j = 0
output = []

ignore = "WUB"
str = str.replace(ignore, " " )

print(re.sub(' +', ' ', str))

        
        
