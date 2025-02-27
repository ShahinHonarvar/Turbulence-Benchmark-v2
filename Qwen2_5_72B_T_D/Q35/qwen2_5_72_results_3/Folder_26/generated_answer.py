from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[68:99])
    duplicates = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in duplicates or not 68 <= s.index(char) < 99))
    return result