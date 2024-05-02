def demo(a):
    b=[]
    avg=sum(a)/len(a)
    b.append(avg)
    for i in a:
        if i>avg:
            b.append(i)
    return b
a=list(map(float,input().split(" ")))
t=tuple(demo(a))
print(t)
