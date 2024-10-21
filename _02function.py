# 想在函数内部更改全局变量，需要用global关键字

money = 500000


def search():
    print(f"您当前的余额为{money}")


def add(num):
    global money
    money +=num
    print(f"操作成功,您当前的余额为{money}")


def sub(num):
    global money
    money -=num
    print(f"操作成功,您当前的余额为{money}")

def main():
    while (1):
        print(
            "1.查询余额\n"
            "2.存款\n"
            "3.取款\n"
            "4.退出系统")
        op = int(input("请输入您要执行的操作代码:"))
        if op == 1:
            search()
        elif op == 2:
            add(int(input("请输入您的存款金额")))
        elif op == 3:
            sub(int(input("请输入您的取出金额")))
        elif op == 4:
            break
        else:
            print("请输入一个有效数字")

while 1:
    name = input("请输入您的用户名: ")
    if name != "liyong":
        print("您输入的用户名错误，请重新输入")
    else:
        main()
        break
