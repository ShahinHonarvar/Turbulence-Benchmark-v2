from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    f = s[:30]
    m = s[30:201]
    l = s[201:]
    c = Counter(m)
    r = set((x for x in c if c[x] > 1))
    return f + ''.join((x for x in m if x not in r)) + l