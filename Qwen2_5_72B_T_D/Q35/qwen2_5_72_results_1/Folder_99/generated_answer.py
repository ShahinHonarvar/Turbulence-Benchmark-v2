from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[450:905])
    repeated_chars = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result