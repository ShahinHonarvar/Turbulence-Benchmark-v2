import collections

def remove_repeat_chars(s):
    count = collections.Counter(s)
    for c in set(s):
        if count[c] > 1:
            s = s.replace(c, '')
    return s