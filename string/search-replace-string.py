import fileinput
import re


replacements = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}

def searchReplace(filename):

    lines = []
    with open(filename) as infile:
        for line in infile:
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            lines.append(line)
    with open(filename, 'w') as outfile:
        for line in lines:
            outfile.write(line)

if __name__ == "__main__" :
    filename='text.txt'
    searchReplace(filename)