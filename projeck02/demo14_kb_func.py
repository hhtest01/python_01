#可变化参数的-字典形式的参数

def show_info(**kwargs):
    print(kwargs)
dt_date = {"x":1,"y":2,"z":3}
print(show_info(a="hello",b="world",c=345))
print(show_info(**dt_date))




def car_start():
    print("车进行启动")


class Elevator():
    button = "开/关"
    floor = 15
    people_nums =13
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