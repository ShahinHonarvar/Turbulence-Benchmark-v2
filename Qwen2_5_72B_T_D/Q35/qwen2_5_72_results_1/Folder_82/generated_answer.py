from collections import Counter

def remove_repeat_chars(s):
    to_check = s[30:200]
    char_count = Counter(to_check)
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))