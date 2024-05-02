import math
def isPrime(n):
    if n<=1:
        return 0
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return 0
        return 1
n=int(input('请输入一个整数：\n'))
if isPrime(n):
    print('是素数')
else:
    print('不是素数')
