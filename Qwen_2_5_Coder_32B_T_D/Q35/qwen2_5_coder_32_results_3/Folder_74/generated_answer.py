from collections import Counter

def remove_repeat_chars(s):
    t = s[70:97]
    c = Counter(t)
    repeat_chars = {k for k, v in c.items() if v > 1}
    return ''.join([char for char in s if char not in repeat_chars])