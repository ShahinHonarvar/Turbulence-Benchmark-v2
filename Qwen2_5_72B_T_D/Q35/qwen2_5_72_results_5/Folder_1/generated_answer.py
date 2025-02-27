from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[17:88])
    repeated_chars = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 17 <= s.index(char) <= 88))
    return result