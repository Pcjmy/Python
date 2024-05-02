import math
a=int(input())
def isPrime(n):
	m=int(math.sqrt(n)+1)
	if n<=1:
		return False
	else:
		for i in range (2,m):
			if n%i==0:
				return False
	return True
flag=False;
while a>1:
	for i in range (1,1000):
		if isPrime(i):
			while(a%i==0):
				if flag==False:
					flag=True
					print("{}={}".format(a,i),end="")
					a=a//i
				else:
					print("*{}".format(i),end="")
					a=a//i
print("\n")