def demo(s):
    result=[0,0,0,0]
    for ch in s:
        if ch.isupper():
            result[0]+=1
        elif ch.islower():
            result[1]+=1
        elif ch>='0' and ch<='9':
            result[2]+=1
        else:
            result[3]+=1
    return tuple(result)
s=input()
result=demo(s)
print('大写字母、小写字母、数字、其他字符的个数分别为：')
print(result)
