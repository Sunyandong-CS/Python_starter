import types

# 使用type()
print(type(123))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type() 判断
class Animal(object):
    pass

print(type(abs))
print(type(Animal()))

print(type(123) == type(456))
print(type(123) == int)
print(type(123) == type('abc'))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x*x) == types.LambdaType)

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 10
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'), obj.x)
print(hasattr(obj, 'y'))

# 动态添加属性
print(hasattr(obj, 'y'), getattr(obj,'y', 404)) # 404为默认值，如果没有'y'则会抛出404
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'), getattr(obj,'y', 404))

# 也可以获取对象方法
print(hasattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())