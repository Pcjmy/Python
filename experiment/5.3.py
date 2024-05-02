import os
def listfile(dirname):
    filelist=[]
    files=os.listdir(dirname)
    for item in files:
        if item[-3:]=='pyc':
            filelist.append(item)
    return filelist
file=listfile(os.getcwd())
for a in file:
    print(a)
