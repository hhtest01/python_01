#格式化字符串：%s
my_str = "my name is %s" % ("张三")
print(my_str)
#格式化整数：%d
my_str1 = "张三 今年 %d 岁,李四只有 %d 岁" % (25,13)
print(my_str1)
#格式化浮点化：%f
my_str2 = "一斤苹果%f元,一斤香蕉%f元" % (5.3,6.7)
print(my_str2)
#辅助命令：m,n
my_str3 = "一斤苹果%5.2f元" %(4.5)
print(my_str3)

#显示左对齐：-
my_str4 = "一斤苹果%-5.2f元" %(4.5)
print(my_str4)
#数字前面显示+：+
my_str5 = "一斤苹果%+8.2f元" %(4.5)
print(my_str5)

#前面使用0代替
my_str6 = "一斤苹果%08.2f元" %(4.5)
print(my_str6)

#使用format去格式化:"{}"
my_str7= "张三 今年{}岁" .format("25")
print(my_str7)

#format格式化两个参数："{} {}".format(参数1，参数2)
my_str8 = "今天星期{},张三买了{}斤苹果".format("三",8)
print(my_str8)
#format的位置参数："{0} {1}".format(第一个数，第二个数)
my_str9 = "今天星期{0},张三买了{1}斤苹果".format("四",9)
print(my_str9)

#format关键字参数："{x} {y}".format(x="hello"，y="work")
my_str9 = "今天星期{x},张三买了{y}斤苹果".format(x="二",y="6")
print(my_str9)

#位置参数和关键字参数结合使用："{0} {y}".format("hello"，y="work")
my_str9 = "今天星期{0},张三买了{y}斤苹果".format("一",y="7")
print(my_str9)

#字符串分割：join(seq)
astr = "hello"
bstr = astr.join("world")
print(bstr)

#分割字符串：split(str="")，其中str代表分隔符
cstr = "hello world python java php"
dstr = cstr.split("o")
print(dstr)

#查找字符串：find(substr),如果找到了返回的最小索引，没找到返回-1
estr = "hellowrold"
print(estr.find("o"))
print(estr.find("l"))
print(estr.find("x"))

#查找xxx结尾的字符串：endwish("xxx")
fstr = "测试报告.doc"
if fstr.endswith(".doc"):
 print("它是一个word文档")


#替换字符串：replace(old_value,new_value)
gstr = "hello world"
hstr = gstr.replace(("world","python"))
print(hstr)


