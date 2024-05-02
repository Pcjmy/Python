s=input()
a=s[-1]
sum=0
b=int(s[0:-2])
if b<=1000:
    sum+=8
else:
    sum+=8
    b=b-1000
    if b%500==0:
        sum+=4*b//500
    else:
        sum+=4*(b//500+1)
if a=='y':
    sum+=5
print(sum)