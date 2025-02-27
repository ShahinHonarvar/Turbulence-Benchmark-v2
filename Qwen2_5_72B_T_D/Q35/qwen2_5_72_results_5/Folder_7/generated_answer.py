from collections import Counter

def remove_repeat_chars(s):
    if len(s) < 927:
        return s
    substring = s[375:926]
    char_count = Counter(substring)
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))