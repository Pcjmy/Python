import re
s=input()
a=re.compile(r'(?P<f>\b\w+\b)\s(?P=f)')
result=a.search(s)
s=s.replace(result.group(0),result.group(1))
print(s)