import re
s=input()
s=re.sub(r'\bi\b','I',s)
print(s)