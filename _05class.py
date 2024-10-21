class student:
    name=None
    age=None
    address=None

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    #魔术方法
    def __str__(self):
        return f"该生名字为{self.name},年龄为{self.age},住址为{self.address}"

i=0
stu_list=[]

while i<2:
    name=input("请输入您的姓名: ")
    age=input("请输入您的年龄: ")
    address=input("请输入您的家庭住址: ")
    stu=student(name,age, address)
    stu_list.append(stu)
    i+=1

for s in stu_list:
    print(s)