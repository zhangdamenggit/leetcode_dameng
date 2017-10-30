# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:10:11 2017

@author: Administrator
"""
#reverse integer
#取余？不知道有多少位
#每一个数字放到数组里？那还是要先取余··
#32位有符号整数的范围？-2^31~2^31
#溢出返回0 如何实现？
#明明有函数却不知道用  只知道硬实现
#cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
#正则！！
#def reverse(self, x):
#x=-1
#s = 1 if x>0 else -1
#s=x>0 and 1 or -1
#max = (a if a > b else b)
#max = (a > b and [a] or [b])[0] #list
#max = (a > b and a or b)
#s=-1
#r=int(str(abs(x))[::-1])
#print(s*r*(r < 2**31))  
#reverse(321)
#s = 'python'
#print (s[::-1])
def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=x>0 and 1 or -1
        r=int(str(abs(x))[::-1])
        return(s*r*(r<2**31))
x=1
print(reverse(1,x))