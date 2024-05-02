def move(n,a,b,c):
    if(n==1):
        print(a+'->'+c)
        return
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)
n=int(input('请输入移动的圆盘的数量：\n'))
move(n,'a','b','c')
