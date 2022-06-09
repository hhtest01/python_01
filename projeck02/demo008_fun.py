#拼接字符串
astr = "+"
btar = astr.join("world")
print(btar)
#拆分字符串
cstr = "hello world python"
dstr = cstr.split(" ")
print(dstr)
#查找字符串的位置
estr = "helloworldpython"
print(estr.find("l"))
print(estr.find("v"))

#判断
fstr = "测试报告.doc"
if fstr.endswith(".doc"):
    print("它是一个word文档")
#替换字符串
gstr = "hello world"
hstr = gstr.replace("world","python")
print(hstr)

#12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
tstr = "sdbc dhvf%$udfv&*%v4574099"
zf = 0
kg = 0
sz = 0
other = 0

for x in tstr:
    if x.isalpha():
        zf += 1
    elif x.isdigit():
        sz +=1
    elif x.isspace():
        kg += 1
    else:
        other +=1
print(zf)
print(kg)
print(sz)
print(other)

