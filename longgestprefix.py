# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:20:17 2017

@author: Administrator
"""

#字符串有比较的方法应该有可以用的方法
#好像并没有可以用的方法
#要一个一个字符比较···
#range(1,5)
#class Solution(object):
#    def longestCommonPrefix(self, strs):
#        """
#        :type strs: List[str]
#        :rtype: str
#        """
#        prefix=""
#        last=strs[0]
#        for str in strs:
#            for i in range(1,len(str)):
#                if str[i]==last[i]:
#                    prefix=prefix+str[i]
#                else:
#                    break
#        
#            last=str
#        return prefix
#这样不是共同的！如何才能找到最长共同？不能是添加 



#

#class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len( strs ) == 0:
            return ''
        if len( strs ) == 1:
            return strs[0]
        minstrslen = 9999
        index = 0
        for i in range( len( strs ) ):
            if len( strs[i] ) < minstrslen:
                minstrslen = len( strs[i] )
                index = i
        ShortestString = strs[index]
        list = [0 for i in range( len( ShortestString ) )]#初始化0        记录有几个str是相同的                    
        for i in range(len( ShortestString )):
            for j in range(len( strs )):
                if strs[j][i] == ShortestString[i]:
                    list[i] += 1
        Prefix = ''
        for i in range( len( ShortestString )):
            if list[i] == len( strs ):
                Prefix += ShortestString[i]
            else:
                break
        return Prefix
##strs=["a","ab"]
##print(strs[0])
#print(Solution.longestCommonPrefix(1,strs))
#
#
#
#




class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index=0
        minlen=9999
        for i in range(len(strs)):
            if len(strs[i])<minlen:
                minlen=len(strs[i])
                index=i
        Shorteststr=strs[index]
        list=[0 for i in range(len(Shorteststr))]
        for i in range(len(strs)):
            for j in range(len(Shorteststr)):
                if strs[i][j]==Shorteststr[j]:
                    list[j]+=1
                else:
                    break
        prefix=""
        for i in range(len(Shorteststr)):
            if list[i]==len(strs):
                prefix+=Shorteststr[i]
            else:
                break
            
        return prefix
strs=["a","ab"]
#print(strs[0])
print(Solution.longestCommonPrefix(1,strs))

#没有前面两个if就会出现 IndexError: list index out of range
#因为如果是空的strs 那么index就没有取值