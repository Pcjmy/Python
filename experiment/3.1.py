a=input()
k=int(input())
b=[]
n=len(a)
for i in range(n):
    if a[i]>='A' and a[i]<='Z':
        s=chr((ord(a[i])+k-ord('A'))%26+ord('A'))
        print(s,end='')
    else:
        s=chr((ord(a[i])+k-ord('a'))%26+ord('a'))
        print(s,end='')