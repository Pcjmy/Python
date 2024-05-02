a,b,c=map(int,input().split())
flag=False
if a+b>c and a+c>b and b+c>a:
    flag=True
if flag==True:
    print("yes")
else:
    print("no")
