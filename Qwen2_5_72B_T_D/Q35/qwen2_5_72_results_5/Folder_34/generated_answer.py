from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[70:200])
    return ''.join((c for c in s if not (70 <= s.index(c) < 200 and counter[c] > 1)))