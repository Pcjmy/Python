with open('data.txt','r') as fp:
    data=fp.readlines()
data=[int(line.strip()) for line in data]
data.sort()
data=[str(i)+'\n' for i in data]
with open('data_new.txt','w') as fp:
    fp.writelines(data)
