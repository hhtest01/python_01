#序列的通用操作
#索引：seq[index],index代表下表，默认从0开始；
lst = ["red","hello",1,3,4]
print(lst[0])
print(lst[-3])

tp = ["red","hello",1,3,4]
print(tp[1])
print(tp[-1])

my_str = "redhello1"
print(my_str[1])
print(my_str[-1])

#序列的切片：seq[start:end:step]start代表开始位置，默认为0；
#end代表结束位置，如果不填则代表列表的长度，step代表的是步长，默认是1
lst2 = ["red","green","blue","black","gold","orange"]
print(lst2[1:5:1])
print(lst2[1:6:2])
print(lst2[2:])


lst3= ["red","green","blue","black","gold","orange","good","bey","hi","work"]
print(lst3[::3])

#序列的相加和相乘
alst = [1,2]
blst = [3,4]
clst = alst+blst
print(clst)

astr = "hello"
bstr = "python"
print(astr+bstr)

dlst = alst * 2
print(dlst)

elst = [None] * 3
print(elst)

print("=" * 60)

#检查元素: in
lst4= ["red","green","blue","black","gold","orange","good","bey","hi","work"]
print("good" in lst4)
print("good1" in lst4)


#序列中的方法
klst = "dsnvcjd"
flst = list(klst)
print(flst)

lst5= ["red","green","blue","black","gold","orange","good","bey","hi","work"]
for index,vls in enumerate(lst5):
    print(index,":",vls)

#列表推导式:[表达式2  循环体 表达式1] 执行顺序：先执行循环体，其次表达式1最后执行表达式2
#例：生成1-10的列表
lst8 = []
for x in range(1,11):
    lst8.append(x)
print(lst8)

lst9 = [x for x in range(1,11)]
print(lst9)
#例：生成1-10的列表，需要打印奇数的数
lst9 = [x for x in range(1,11) if x % 2!=0]
print(lst9)

#例：生成1-10的列表，需要打印奇数的数再加上10
lst9 = [x+10 for x in range(1,11) if x % 2!=0]
print(lst9)