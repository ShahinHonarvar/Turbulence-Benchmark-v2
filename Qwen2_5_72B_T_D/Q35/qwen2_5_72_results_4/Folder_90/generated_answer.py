from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 306 or len(s) <= 807:
        return s
    sub_str = s[306:807]
    char_count = Counter(sub_str)
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result