import re
s=input()
s=re.sub(r'\BI\B','i',s)
print(s)