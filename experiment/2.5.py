n=int(input())
if n%4==0 and n%100!=0 or n%400==0:
    print("是闰年")
else:
    print("不是闰年")