import random
x = [random.randint(0,100) for i in range(50)]
print("the original list:")
print(x)
for i in range(len(x))[::-1]:
    if x[i]%2 == 1:
        del x[i]
print("after delete the list is:")
print(x)