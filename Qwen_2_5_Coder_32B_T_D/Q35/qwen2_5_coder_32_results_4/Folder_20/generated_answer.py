from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 96:
        return s
    target_section = s[28:96]
    char_count = Counter(target_section)
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))