alst = []
blst = [12,"sfjds",13.4,""]
#print(alst)
#print(blst)

#for x in blst:
    #print("列表中的值:",x)
clst = ["red","green","blue",]
clst.append("black")
print(clst)
print(clst.count("green"))
clst.extend(blst)
print(clst)
print(clst.index("black"))
clst.insert(2,"good")
print(clst)
print(clst.pop(6))

for x  in range(0,11,2):
    print(x)
