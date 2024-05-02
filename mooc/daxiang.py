h,r=map(int,input().split())
pi=3.14159
v=pi*r*r*h
m=20000/v
if m==int(m):
    print("%.f"%m)
else:
    x=int(m)+1
    print("%.f"%x)