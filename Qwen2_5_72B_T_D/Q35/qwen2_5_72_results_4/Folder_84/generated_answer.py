from collections import Counter

def remove_repeat_chars(s):
    counts = Counter(s[32:44])
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or not 32 < s.index(char) < 44))