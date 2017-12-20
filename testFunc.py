def trim(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    else:
        return s

s = "     sssss     sssssssss   "
print(trim(s))

def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    maxNum = 0
    minNum = 0
    for i in L:

        if i >= maxNum:
            maxNum = i
        elif i<minNum:
            minNum = i

    return (minNum,maxNum)

l = [1,2,3,4,5,6,6,7,7,8,5,4,3,3]

print(findMinAndMax(l))

L = ['Hello','World',18,'APPLE']
l2 = [s.lower() for s in L if isinstance(s,str) == True]

print(l2)


