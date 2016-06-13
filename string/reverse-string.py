class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return "".join(s[i] for i in range(len(s) - 1, -1, -1))


if __name__ == "__main__":
    result = Solution.reverseString(Solution(), "aabb")
    print result
