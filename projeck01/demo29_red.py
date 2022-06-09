try:
    f = open("a.txt","r")
    while True:
        line = f.readline()
        print(2/0)
        if not line:
            break

except Exception as a:
    print(a)

finally:
    f.close()


def div(x,y):
    try:
        z = x / y
        return z
    except Exception as e:
        print("除法中除数不能为0")
print(div(1,3))
print(div(4,0))
print(div(6,6))
print(__name__)