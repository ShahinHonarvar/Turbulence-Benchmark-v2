from collections import Counter

def remove_repeat_chars(s):
    c = Counter(s[1:9])
    repeat_chars = {k for k, v in c.items() if v > 1}
    return ''.join((x for x in s if x not in repeat_chars))