from collections import Counter

def remove_repeat_chars(s):
    section = s[18:60]
    counts = Counter(section)
    repeated_chars = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 18 <= s.index(char) < 60))
    return result