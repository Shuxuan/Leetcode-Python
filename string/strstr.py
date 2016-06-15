class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0;
        j = 0
        if (len(needle) == 0):
            return 0
        next = self.getNextArr(needle)
        while (i < len(haystack) and j < len(needle)):
            if (haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1

        rst = -1
        if (j == len(needle)):
            rst = i - j
        return rst

    def getNextArr(self, needle):
        next = [0 for i in range(len(needle))]
        j = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[j]:
                next[i] = j + 1;
                j += 1
                i += 1
            else:
                if j > 0:
                    j = next[j - 1]

                else:
                    next[i] = 0
                    i += 1
        return next

