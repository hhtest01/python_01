class Students():

    def __init__(self,name,graed):
        self.name = name
        self.graed = graed

    def study(self):
        self.name = "张三"
        self.graed = "5年级"
        print(self)
        #print("{}年级的{}正在学习".format(self.graed,self.name))
    def eat(self):
        print(self.name,"是",self.graed,"正在吃饭")
s = Students("张三","5年级")
#print(s.study())
print(s.eat())

class Students1():
    def study1(self,name):
        val = "hello"
        print("{} {}".format(val,name))
s1 = Students1()
s1.study1("张三")




