from collections import Counter

def remove_repeat_chars(s):
    substring = s[57:84]
    char_count = Counter(substring)
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result