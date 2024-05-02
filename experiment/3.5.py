import re
s=input('please input a string:\n')
pattern=re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(s))