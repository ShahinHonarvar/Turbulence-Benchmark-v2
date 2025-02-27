from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[57:85])
    duplicates = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in duplicates or not 57 <= s.index(char) < 85))
    return result