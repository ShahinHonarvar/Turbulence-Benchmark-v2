from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s)
    result = ''.join((c for c in s if counter[c] == 1 or (s.index(c) < 200 or s.index(c) >= 202)))
    return result