def demo(v):
    print("最大值：%d"%max(v))
    print("所有整数之和：%d"%sum(v))
a=list(map(int,input().split(" ")))
demo(a)