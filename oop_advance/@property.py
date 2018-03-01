# Pyhon 内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 -100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，
    # 而是通过getter和setter方法来实现的。
    #还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

    @property
    def age(self):
        return 2015 - self._birth

# @property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
# 于是，我们就拥有一个可控的属性操作：

s = Student()
s.score = 99
print('score: ', s.score)
s.birth = 1994

print('age', s.age)
s.age = 55 # wrong AttributeError: can't set attribute
