#生成器（Generators）是一种特殊的迭代器，它们通过 yield 关键字逐步产生值，而不是像普通函数那样一次性返回所有结果。
# 生成器的一个关键特性是惰性计算，即它们只在需要时才生成值，这使得它们特别适合处理大量数据或者无限序列。
#------创建生成器的两种方式
#01 yield
#生成器函数
def simple_generator():
    yield 1
    yield 2
    yield 3
#调用生成器函数时，函数不会立即执行，而是返回一个生成器对象，每次调用next方法，函数会继续运行直到下一个yield。
#再次调用next，函数会从上次yield暂停的地方继续执行。生成器的状态保存
gen=simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
#无限生成器
def infinite_generator():
    n=0
    while True:
        yield n
        n+=1
counter=infinite_generator()
#可以无线调用next(counter)，生成连续函数
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib_gen=fibonacci()

for _ in range(5):
    print(next(fib_gen))