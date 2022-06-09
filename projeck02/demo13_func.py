#函数：其有特定的功能的代码块，比如说登录功能，相加
"""
def 函数名字（参数列表）
    代码块
"""
#函数的定义：加法
def add(x,y):
    z = x+y
    return z          #return的作用：返回函数的执行值

#函数的调用
print(add(3,4))
print(add("特大","功能"))


#函数：位置参数
def add1(x1,y1):
    return x1 + y1

print(add1(3,4))
print(add1("hello","world"))
print(add1("$","$"))



#关键字参数
def student_lesson(grade,subject):
    z1 = "{}年级上{}课".format(grade,subject)
    return z1
print(student_lesson(grade=2,subject="语文"))
print(student_lesson(subject="语文",grade=2))


def job_lesson(grade,good):
    info = ("{}上早班")


def add2(x2,y2,*args):
    print(args)
    z2 = x2+y2 + sum(args)
    return z2
    return None
print(add2(3,4))
print(add2(3,4,5))
print(add2(3,4,5,6,7,8))
print(add2(3,4,*[5,6,7,8]))


