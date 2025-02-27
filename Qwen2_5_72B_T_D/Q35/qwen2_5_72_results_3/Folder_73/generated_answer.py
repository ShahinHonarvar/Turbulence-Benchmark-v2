from collections import Counter

def remove_repeat_chars(s):
    count = Counter(s[10:76])
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 10 <= s.index(char) < 76))
    return result