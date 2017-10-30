# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:08:11 2017

@author: Administrator
"""

#class Solution:
#    def isPalindrome(self, x):
#        """
#        :type x: int
#        :rtype: bool
#        """
#        s=x>=0 and 1 or -1
#        if s==-1:
#            return False
#        r=int(str(abs(x))[::-1])
#        if r>2**31:
#            return False
#        else:
#            if r==x:
#                return True
#            else:
#                return False
#不能使用额外空间 变成字符串就是使用额外空间了
#因为 Python 语言本身的特性，这里反转整数时不需要考虑溢出？？？？
#数字能被十整除的肯定不是回文
#p2  5/2=2 5.0/2=2.5
#p3 5/2=2.5 5//2=2
#class Solution:
#    # @return a boolean
#    def isPalindrome(self, x):
#        if x < 0:
#            return False
#        div = 1
#        while x//div >= 10:
#            div = div * 10
#            
#        while x:
#            left = x // div
#            right = x % 10
#            
#            if left != right:
#                return False
#            
#            x = ( x % div ) // 10
#            div = div // 100
#        return True

def isPalindrome(self, x):
    if x < 0: return False
    k = 1
    while x // k >= 10: k *= 10
    while x > 0:
        if x // k != x % 10: return False
        x = (x - x // k * k) // 10
        k //= 100
    return True
x=12331
a=isPalindrome(1,x)
#从两头开始比较 比较相同后再去掉两头继续比较