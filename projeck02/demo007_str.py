my_str = "my name is %s" % ("张三")
print(my_str)

my_str1 = "张三今年 %d 岁" % (22)
print(my_str1)

my_str2 = "一斤苹果%15.2f元"%(5.6)
print(my_str2)


my_str2 = "一斤苹果%-15.2f元"%(5.6)
print(my_str2)


my_str2 = "一斤苹果%+15.2f元"%(5.6)
print(my_str2)
my_str2 = "一斤苹果%08.2f元"%(5.6)
print(my_str2)


my_str3= "my name is {}".format("张三")
print(my_str3)

my_str4 = "今天星期{},张三买了{}斤苹果".format("二",8)
print(my_str4)

my_str5 = "张三选修{},李四选修{}".format("java","python")
print(my_str5)

my_str6 = "张三选修{x},李四选修{y}".format(x="java",y="python")
print(my_str6)


my_str7 = "张三选修{0},李四选修{y}".format("java",y="python")
print(my_str7)


