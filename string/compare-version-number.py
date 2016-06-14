class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = version1.split('.')
        v2 = version2.split('.')


        l1 = len(v1)
        l2 = len(v2)

        index1 = 0
        index2 = 0

        while (index1 < l1 and index2 < l2) :
            if (int(v1[index1]) > int(v2[index2])) :
                return 1
            elif (int(v1[index1]) < int(v2[index2])) :
                return -1
            index1 += 1
            index2 += 1

        while (index1 < l1) :
            if (int(v1[index1]) > 0) :
                return 1
            index1 += 1

        while (index2 < l2):
            if (int(v2[index2]) > 0):
                return -1
            index2 += 1

        return 0

if __name__ == '__main__' :
    version1 = '1'
    version2 = '1.1'
    rst = Solution.compareVersion(Solution(), version1, version2)
    print rst
