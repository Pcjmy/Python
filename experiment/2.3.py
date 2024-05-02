import random
a=[random.randint(1,100) for i in range(20)]
print(a)
a[::2]=sorted(a[::2],reverse=True)
print(a)