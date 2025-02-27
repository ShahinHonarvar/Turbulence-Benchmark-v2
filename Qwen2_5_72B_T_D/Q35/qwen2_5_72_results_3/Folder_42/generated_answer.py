from collections import Counter

def remove_repeat_chars(s):
    sub_s = s[18:60]
    char_count = Counter(sub_s)
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 18 <= s.index(char) < 60))
    return result