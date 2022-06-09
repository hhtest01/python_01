#1.输入a,b,c,d 4个整数，计算a+b-c*d的结
a = input("请输入一个整数:")
b = input("请输入一个整数:")
c = input("请输入一个整数:")
d = input("请输入一个整数:")
print(int(a)+int(b)-int(c)*int(d))
#2.打印1~100内被3整除的所有数的和 。
sum = 0
for x1 in range(1,101):
    if x1 % 3 == 0:
       sum += x1
print(sum)
#3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2):
    print("输出1~10内的所有奇数",x)
#4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x2 in range(1,101):
    if x2 % 2 == 0:
       sum1 += x2
    else:
        sum2 += x2
print("偶数和:",sum1)
print("奇数和为:",sum2)
print(sum1-sum2)
#5. 求1+2+3+...+100的和
m = 1
sum3 = 0
for m in range(1,101):
    sum3 += m
    m += 1
print(sum3)
#6. 判断一个数n能同时被3和5整除
n1=input("请输入一个整数:")
if int(n1) % 3 ==0 and int(n1) % 5 ==0:
    print(n1,"能被3和5同时整除")
else:
    print(n1,"不能被3和5同时整除")



#7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
v = input("请输入一个整数：")
if 1<int(v)<100:
    print("是")
else:
    print("不是")
#8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
lst = []
x = input("请输入一个整数：")
y = input("请输入一个整数：")
z = input("请输入一个整数：")
lst.append(int(x))
lst.append(int(y))
lst.append(int(z))
print(lst)
lst.sort()
print(lst)
print("=========================================")
#9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
#10. 将一个列表的数据复制到另一个列表中。
#11. 输出 9*9 乘法口诀表。
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




#13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#14. 题目：打印出如下图案（菱形）:
star1 = "*"
a = [1,3,5,7,5,3,1]
for i in a:
    print((star1*i).center(7))
