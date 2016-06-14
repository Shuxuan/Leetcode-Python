from sets import Set

import re


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = re.findall('(?i)[aeiou]', s)

        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        left = 0
        right = len(s) - 1
        ls = list(s)
        while (left < right):
            while (left < len(s) and s[left] not in vowels):
                left += 1
            while (right >= 0 and s[right] not in vowels):
                right -= 1
            if (left < right):
                ls[left], ls[right] = ls[right], ls[left]
            left, right = left + 1, right - 1

        return ''.join(ls)

if __name__ == '__main__' :
    str = 'hello'
    rst = Solution.reverseVowels(Solution(), str)
    print rst

