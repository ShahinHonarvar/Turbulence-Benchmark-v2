from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[56:90])
    repeat_chars = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or not 56 <= s.index(char) < 90))
    return result