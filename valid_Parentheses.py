#不仅仅需要个数正确，还需要括号内也是有效括号，也即，（【）】并不是有效括号
#建字典？
#class Solution:
#    def isValid(self, s):
#        """
#        :type s: str
#        :rtype: bool
#        """
#        dic={
#            '(':')',
#            '[':']',
#            '{':'}'
#        }
#        
#        if len(s)%2!=0:
#            return False
#        else:
#            for i in range(len(s)):
#                if dic[s[i]]==s[(len(s)-i-1)]:
#                    return True
#                else:
#                    return False
#            

#用栈来解决~~~


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
#            if s[i] == ']':
#                if stack == [] or stack.pop() != '[':
#                    return False
#            if s[i] == '}':
#                if stack == [] or stack.pop() != '{':
#                    return False
        if stack:
            return False
        else:
            return True
#匹配后弹栈如何体现的   竟然自动？？？！！
s='()'
print(Solution.isValid(1,s))