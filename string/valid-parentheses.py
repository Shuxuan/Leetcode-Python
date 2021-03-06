class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for ch in s :
            if ch == '(' or ch == '{' or ch == '[' :
                stack.append(ch)
            else :
                if not stack :
                    return False

                if ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{' or ch == ']' and stack[-1] != '[' :
                    return False

                stack.pop()

        return not stack

if __name__ == '__main__' :
    s = '()(()'

    rst = Solution.isValid(Solution(), s)

    print rst