from collections import Counter

def remove_repeat_chars(s):
    to_check = s[46:91]
    char_count = Counter(to_check)
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))