from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[69:97])
    repeated_chars = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for i, char in enumerate(s) if char not in repeated_chars or i < 69 or i >= 97))
    return result