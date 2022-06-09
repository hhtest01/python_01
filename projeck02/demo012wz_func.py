
def start():
    print("车进行启动")

def run():
    print("车在行驶")
start()
run()



class Elevator():
    button = "开/关"
    floor = 15
    pepole_nums = 13
    def start(self):
        print("打开电梯")
    def stop(self):
        print("关闭电梯")
    def run(self):
        print("电梯运行")
e = Elevator()
e.start()
e.stop()
e.run()

class Students1():
    def __init__(self,name,graed):
        self.name = name
        self.graed = graed
        print()
    def study(self):
        print("{}年级的{}正在学习".format(self.graed,self.name))
s3 = Students1("王五",8)
s3.study()




class Students():

    def __init__(self):
        print()
    def study(self):
        print(self)
        print("{}年级的{}正在学习".format(self.graed,self.name))
s1 =Students()
print(s1)
s1.graed = 3
s1.name = "lisi"
print(s1.study())

s2 = Students()
print(s2)
s2.graed = 5
s2.name = "zhangsan"
print(s2.study())





