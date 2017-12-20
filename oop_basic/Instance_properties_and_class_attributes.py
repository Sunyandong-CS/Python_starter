class Student(object):
    name = 'student'
    def __init__(self):
        self.name = 'bob'

student = Student()
print(student.name) # bob 会优先访问实例对象的属性

del student.name # 删除实例对象的属性就会访问到类的属性
print(student.name) # student 会访问class的属性


# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student_Count(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student_Count.count += 1

# 测试:
if Student_Count.count != 0:
    print('测试失败!')
else:
    bart = Student_Count('Bart')
    if Student_Count.count != 1:
        print('测试失败!')
    else:
        lisa = Student_Count('Bart')
        if Student_Count.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student_Count.count)
            print('测试通过!')