lst = []
for x in range(1,11):
    lst.append(x)
print(lst)


lst1 = [x for x in range(1,11)]
print(lst1)
lst2 = [x+10 for x in range(1,11) if x % 2 !=0]
print(lst2)

num = 5
x1 = num - 1
for n in range(1,5):
    print(n)