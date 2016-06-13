def reverseString(s):

    # https://leetcode.com/problems/reverse-string/

    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

def main():
    s = reverseString("aabb")
    print s

if __name__ == "__main__": main()



