from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    sub = s[45:78]
    char_count = Counter(sub)
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))