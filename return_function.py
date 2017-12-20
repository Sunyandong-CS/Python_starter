# 练习
#
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    n = 0
    def counter():
        nonlocal n # nonlocal - 用于操作外层作用域中的对象。
        n += 1
        return n
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())