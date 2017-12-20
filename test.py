# -*- coding:utf-8 -*-

#  计算BMI

height = float(input('输入身高:'))
weight = float(input('输入体重:'))

bmi = weight / (height * height)
print('您的BMI为:%0.2f' %bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')


