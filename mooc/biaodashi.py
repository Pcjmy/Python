a,b,c=input().split();
a=int(a);
b=int(b);
if c=='+':
    res=a+b
    print(res)
elif c=='-':
    res=a-b
    print(res)
elif c=='*':
    res=a*b
    print(res)
elif c=='/':
    if b==0:
        print("Divided by zero!")
    else:
        res=int(a//b)
        print(res)
else:
    print("Invalid operator!")
