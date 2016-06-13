def reverseString(s):

    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

def main():
    s = reverseString("aabb")
    print s

    print "".join(s[i] for i in range(len(s) - 1, -1, -1))


if __name__ == "__main__": main()

