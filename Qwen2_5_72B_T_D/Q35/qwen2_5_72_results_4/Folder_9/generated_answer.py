from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 80 or len(s) <= 200:
        return s
    substring = s[80:200]
    char_counts = Counter(substring)
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result