from collections import OrderedDict

def remove_repeat_chars(s):
    unique_chars = OrderedDict.fromkeys(s[125:825])
    return ''.join((char for char in s if char not in unique_chars or sum((1 for c in s.count(char) if 125 < s.index(c) < 825)) == 1))