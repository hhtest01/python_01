#条件语句
"""
if 条件语句:
    执行代码块
"""
a=13
if a>10:
    print("a是大于10的数")
else:
    print("a是小于10的数")
"""
if 条件判断1:
    代码1 
elif 条件判断2:
    代码2
elif 条件判断3：
    代码3 
else:
    代码4
"""
score = 76
if score >= 90:
    print("优秀")
elif score >= 88:
    print("良")
elif score >= 68:
    print("及格")
else:
    print("不及格")
if score > 75 and score < 90:
    print("良")

if 1:
    print("hello world")
if 0:
    print("hello world01")
print("=========================================")
if "a":
    print("hello world01")
if " ":
    print("hello world01")

a_str = "hello"
b_str = "hello world"
print(a_str in b_str)

