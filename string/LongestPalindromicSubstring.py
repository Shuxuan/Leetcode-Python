class Solution:

    # DP approach (4000ms+)
    def longestPalindrome(self, s: str) -> str:
        if (len(s) < 2) :
            return s

        dp = [[False for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
        start = 0;
        maxLen = 0;
        for i in range(len(s) - 1):
            if (s[i] == s[i+1]):
                dp[i][i+1] = True
                start = i;
                maxlen = 2;

        for k in range(3, len(s)+1):
            for i in range(0, len(s)-k + 1):
                j = i + k - 1;
                if (dp[i+1][j-1] == True and s[i] == s[j]):
                    dp[i][j] = True
                    if (k > maxLen) :
                        maxLen = k;
                        start = i;

        return s[start, start + maxLen]


    def __init__(self) :
        print("init")

def main():
    s = "babad"
    obj = Solution();
    output = obj.longestPalindrome(s);
    print(output)

if __name__=='__main__':
    main()