class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

    def __init__(self):  # special method to initialize
        print("init")

def main():
    num1 = "111"
    num2 = "1"
    s = Solution()
    output = s.addStrings(num1, num2)
    print(output)


if __name__ == '__main__':
    main()