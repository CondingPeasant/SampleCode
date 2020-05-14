import sys

def add(lh, rh):
    return lh + rh

def abstract(lh, rh):
    return lh - rh

def multiply(lh, rh):
    return lh * rh

def divide(lh, rh):
    return lh / rh

def main(argv):
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    x = int(argv[1])
    y = int(argv[2])

    print(str(x) + "+" + str(y) + "=" +str(add(x, y)))
    print(str(x) + "-" + str(y) + "=" +str(abstract(x, y)))
    print(str(x) + "*" + str(y) + "=" +str(multiply(x, y)))
    print(str(x) + "/" + str(y) + "=" +str(divide(x, y)))

if __name__ == "__main__":
   main(sys.argv)

# 可写函数说明
# sum = lambda arg1, arg2: arg1 + arg2
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))


