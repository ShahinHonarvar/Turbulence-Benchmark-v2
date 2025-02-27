from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    target = s[18:88]
    counts = Counter(target)
    repeats = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeats))