from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[80:200]
    char_count = Counter(sub)
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))