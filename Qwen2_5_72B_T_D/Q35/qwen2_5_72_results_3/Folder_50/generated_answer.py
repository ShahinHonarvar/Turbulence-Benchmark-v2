from collections import Counter

def remove_repeat_chars(s):
    counts = Counter(s[13:76])
    result = ''.join((c for i, c in enumerate(s) if i < 13 or i >= 76 or counts[c] < 2))
    return result