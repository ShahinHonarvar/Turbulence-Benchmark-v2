from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 355 or len(s) <= 988:
        return s
    sub_str = s[355:988]
    char_count = Counter(sub_str)
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))