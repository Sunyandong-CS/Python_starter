# python是个动态语言，我们可以很轻易的给一个类一个对象添加属性
class Student(object):
    def __init__(self, name):
        self.name = name

# 创建一个对象，并添加一个属性
s1 = Student('mike')
s1.age = 19
print(s1.age)

# 创建一个对象，并添加一个方法
s2 = Student('jack')
def call(self):
    print('%s is make phone call' % (self.name))

from types import  MethodType
s2.call = MethodType(call,s2)
s2.call()
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student_Slot(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student_Slot()
s.name = 'Michael'
s.age = 24
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

try:
    s.mark = 66
except AttributeError as e:
    print('AttributeError:', e)