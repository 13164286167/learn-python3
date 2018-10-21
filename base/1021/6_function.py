#调用内置函数
n1 = 255
print(hex(n1))

#自定一函数
import math
def quadratic(a,b,c):
    fz =math.sqrt(b * b - 4 * a * c)
    x1 =( -b + fz )/ (2 * a) 
    x2 =( -b - fz )/ (2 * a) 
    return  x1,x2
a = quadratic(1,1,0)
print(a)
#关键字参数
def myfun(a,b,**key):
    print(a,b,key)
myfun(1,2,num=123)
#可变参数
def mul(*nums):
    res = 1
    for num in nums:
        res = res * num 
    print(res)
mul(1,2,3,4,5)