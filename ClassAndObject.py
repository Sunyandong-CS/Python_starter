# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：



# 创建一个类
class Student(object):

    def __init__(self, name, gender ,score):
        self.name = name   # self.name表示公共变量
        self.__score = score # self.__score表示私有变量
        self.__gender = gender # 私有属性,性别

    # get方法，用于获取私有变量的值
    def get_score(self):
        return self.__score
    def get_gender(self):
        return self.__gender
    # set方法用于修改私有变量
    def set_score(self, score):
        self.__score = score
    def set_gender(self, gender):

        # 数据有效性检测
        sex = ['male', 'female']
        if gender in sex:
            self.__gender = gender
        else:
            raise ValueError('性别只能为 male \ female')

    def print_score(self):
        print('%s: %s---%s' % (self.name, self.__score, self.get_grade()))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'

# 实例化一个对象
bart = Student('jack', 88, 'female')
bart.name = 'simos'
bart.set_score(80)

print(bart.name, bart.get_score() ,bart.get_grade())
# 调用对象方法
bart.print_score()
bart.set_gender('male')
print(bart.get_gender())
