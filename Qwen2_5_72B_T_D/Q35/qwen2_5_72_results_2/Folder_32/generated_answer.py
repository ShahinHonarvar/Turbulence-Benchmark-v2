from collections import Counter

def remove_repeat_chars(s):
    substr = s[86:90]
    counts = Counter(substr)
    repeated_chars = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result