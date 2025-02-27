from collections import Counter

def remove_repeat_chars(s):
    substring = s[81:86]
    char_count = Counter(substring)
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result