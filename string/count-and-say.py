class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rst = '1'

        s = '1'
        for i in xrange(n - 1):
            prev = newS = ''
            num = 0
            for curr in s:
                if prev != '' and prev != curr:
                    newS += str(num) + prev
                    num = 1
                else:
                    num += 1
                prev = curr
            newS += str(num) + prev
            s = newS
        return s



if __name__ == "__main__" :
    n = 4
    rst = Solution.countAndSay(Solution(), n)
    print rst


