from collections import Counter

def remove_repeat_chars(s):
    if len(s) < 989:
        return s
    t = s[356:988]
    c = Counter(t)
    r = set((x for x in c if c[x] > 1))
    return ''.join((x for x in s if x not in r))