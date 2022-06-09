def add(x,y):
    z = x + y
    return z
print(add(3,4))
print(add("hello","world"))



def div(x,y):
    return x / y
print(div(3,9))



def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z
print(student_lesson(grade=2,subject="语文"))
print(student_lesson(3,subject="语文"))

def study_language(name,languge="python"):
    info = "{}要学习{}语言".format(name,languge)
    return info
print(study_language("张三","java"))
print(study_language("lisi","c++"))
print(study_language("wangwu"))


def add1(x,y,*args):
    print(args)
    z1 = x+y+sum(args)
    return z1

print(add1(3,4))
print(add1(3,4,5))
print(add1(3,4,5,7,8))
print(add1(3,4,*[1,2,3,4,5,6]))

dt_data = {"x":1,"y":2,"c":3}
def show_info(**kwargs):
    print(kwargs)
print(show_info(a="hello",b="world",c=3))
print(show_info(**dt_data))


def show_info1(*args,**kwargs):
    print(args,kwargs)
