filename="program.txt"
with open(filename,'w') as obj:
    obj.write("I love programming.\n")
    obj.write("python is powerful.\n")
with open("program.txt") as obj:
    contents=obj.read()
    print(contents)
