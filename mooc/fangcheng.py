import math
a,b,c=map(float,input().split())
if b*b==4*a*c:
    y=-b/(2*a)
    print("x1=x2=%.5f"%y)
elif b*b>4*a*c:
    y1=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    y2=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    if y1<y2:
        y1,y2=y2,y1
    print("x1=%.5f;x2=%.5f"%(y1,y2))
else:
    y=-b/(2*a)
    y1=math.sqrt(4*a*c-b*b)/(2*a)
    if y==0:
        print("x1=0.00000+%.5fi;x2=0.00000-%.5fi"%(y1,y1))
    else:
        print("x1=%.5f+%.5fi;x2=%.5f-%.5fi"%(y,y1,y,y1))
