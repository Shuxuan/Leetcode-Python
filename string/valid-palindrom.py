import re


class Solution(object):
    def isPalindrom(self, s):
        if s == '' :
            return True

        s = re.findall('[a-zA-Z0-9]', s)
        size = len(s)

        for x in range(size/2) :
            if s[x].lower() != s[size-1-x].lower() :
                return False

        return True

if __name__ == '__main__' :
    s = '09'
    print Solution.isPalindrom(Solution(), s)