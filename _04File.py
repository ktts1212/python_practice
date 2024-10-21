f = open("C:/Users/liyong/Desktop/ceshi.txt","r",encoding="UTF-8")
count=0
for x in f:
    list=x.replace("\n","").split(" ")
    print(list)
    for y in list:
        if y=="itheima":
            count+=1
print(count)
f.close()

f=open("C:/Users/liyong/Desktop/ceshi.txt","a",encoding="UTF-8")
f.write("liyong itheima python\n")
f.close()