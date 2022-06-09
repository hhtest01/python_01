f = open("a.txt","r")
result = f.read()
print(result)
f.close()


f1 = open("a.txt","w")
f1.write("hello php\n")
f1.write("hello java")
f1.close()
