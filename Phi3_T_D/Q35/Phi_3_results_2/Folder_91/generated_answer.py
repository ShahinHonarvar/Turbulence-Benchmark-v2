from collections import OrderedDict

def remove_repeat_chars(s):
    return ''.join(OrderedDict.fromkeys((c for i, c in enumerate(s) if 0 < i < 6 and s[i - 1] != c and (i == 5 or s[i + 1] != c))))