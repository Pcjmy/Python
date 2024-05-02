a=float(input())
if 0<=a<5:
    sum=-a+2.5
elif 5<=a<10:
    sum=2-1.5*(a-3)*(a-3)
elif 10<=a<20:
    sum=a/2-1.5
print("%.3f"%sum)