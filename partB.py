'''
@author: Christophe Yuen Sang
'''
import sys  # library for the command line
import re   # library for regular expression
from collections import defaultdict # library for default dictionary


def open_file(filename, mode):
    while True:
        try:
            file = open(filename,mode)
            return file
        except IOError:
            print("Can't open " + filename + "!")
            filename = input("Please enter a valid file: ")


def parse_from(filename):
    # \W = [^a-zA-Z0-9]
    pattern = re.compile('\W')
    file = open_file(filename, "r")
    for line in file:
    # create a list of string separated by anything that is not a-z & A-Z & 0-9.
        for word in (pattern.split(line)):
        # filter out empty string because regex.split create empty string when multiple matches
        # are adjacent to one another, an empty string is inserted into the array.
            if word:
                yield word.lower()


def create_dictionary_from(filename):
    str_dict = defaultdict(int)
    
    for word in parse_from(filename):
        str_dict[word] += 1
        
    return str_dict


def intersect_between(filename1, filename2):
    str_dict1 = create_dictionary_from(filename1)
    str_dict2 = create_dictionary_from(filename2)
    common = set();
    
    for k in str_dict1.keys():
        if str_dict2[k]:
            common.add(k)
            
    return common


def print_intersect(s):
    print("\nIntersect:" ,sorted(s))
    print("Total:", len(s))


def print_dictionary(d):
    # sorted first in decreasing order for the frequency (-i[1]) then in alphabetical order (i[0])
    print("n# of tokens:", len(d))
    for (k, v) in sorted(d.items(), key = (lambda i: (-i[1] ,i[0]))):
        print(k + " -", v)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print_intersect(intersect_between(sys.argv[1], sys.argv[2]))
    else:
        print("Invalid number of argument!")