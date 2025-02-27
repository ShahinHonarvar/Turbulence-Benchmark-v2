from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 355 or len(s) <= 988:
        return s
    substring = s[355:988]
    char_count = Counter(substring)
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result