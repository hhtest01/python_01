class Students():
    name = "张三"
    grade = "5年级"

    def __init__(self):
        print()
    def study(self):
        print(self)
        print("{}年级的{}正在学习".format(self.graed,self.name))



print(Students.name)
print(Students.grade)
print("="*60)
s = Students
print(s.name)
print(s.grade)