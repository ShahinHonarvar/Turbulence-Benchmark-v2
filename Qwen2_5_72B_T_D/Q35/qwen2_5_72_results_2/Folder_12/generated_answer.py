from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 16 or len(s) <= 87:
        return s
    sub_s = s[16:87]
    char_count = Counter(sub_s)
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result