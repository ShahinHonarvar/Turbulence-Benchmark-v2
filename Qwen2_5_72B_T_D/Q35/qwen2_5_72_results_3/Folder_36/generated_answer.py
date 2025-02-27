from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[476:709])
    repeated_chars = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 476 <= s.index(char) < 709))
    return result