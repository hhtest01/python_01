class People():
    age =  0

    def eat(self,people_type):
        print(people_type,"在吃饭")



class Stuedents(People):
    def eat(self,graed):
        super().eat(graed)
        print(graed,"正在吃饭")
class Teacher(People):
    def eat(self,subject,time):
        print("{}的老师，{}在食堂吃饭".format(subject,time))

s = Stuedents()
s.eat("2年级")
#Stuedents.age = "20"
#print(Stuedents.age)

t = Teacher()
t.eat("语文学科","12:00")
#Teacher.age = "40"
#print(Teacher.age)