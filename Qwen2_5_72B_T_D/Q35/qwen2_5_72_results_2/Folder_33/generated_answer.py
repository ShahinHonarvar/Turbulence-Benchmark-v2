from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 825:
        return s
    substring = s[125:825]
    char_count = Counter(substring)
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 125 <= s.index(char) < 825))
    return result