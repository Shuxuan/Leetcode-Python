class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])

def main():
    a = "11"
    b = "1"
    test = str(bin(int(a, 2) + int(b, 2)))
    print(test)
    ret = Solution().addBinary(a, b)
    print(ret)

if __name__ == '__main__':
    main()
