from  functools import reduce

def fn(x,y):
    return x*10 + y
def charToInt(s):
    return {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}[s]

num = reduce(fn,map(charToInt,'123456'))
print(num)

print(isinstance(num,int))


## 大小写转变
def tonomal(s):
    return  s.capitalize()
def nomalize(name):
    return  map(tonomal,name)

s = ['adas','SSSSS','barT']

s1 = nomalize(s)
for s2 in s1:
    print(s2)

def multify(x,y):
    return  x * y

def prod(L):
    return  reduce(multify,L)

l = [1,2,3,4,5]

sum1 = prod(l)
print(sum1)

# 字符串转数字

def str2float(s):
     n = s.index('.')
     return reduce(fn,map(charToInt,s[:n]+s[n+1:])) / pow(10,len(s) - n -1)

l1 = '123.456'

print(str2float(l1))


def is_palindrome(n):
    str_int = str(n)
    return str_int == str_int[::-1]

output = filter(is_palindrome,range(1,1000))
print('1---1000',list(output))

l3 = [1111,2222,43434,556,76443]
for l in l3:
    print(is_palindrome(l))

l4 = [('Bob',77),('Lisa',98),('Mike',88)]
def by_name(t):
    return t[0]
l5 = sorted(l4,key=by_name)

print(l5)


