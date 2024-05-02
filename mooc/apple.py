n,x,y=map(int,input().split())
a=y//x
if y%x!=0:
    a+=1
n=n-a
if n<0:
    n=0
print(n)