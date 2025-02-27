from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[51:76])
    for char, count in counter.items():
        if count > 1:
            s = s.replace(char, '')
    return s