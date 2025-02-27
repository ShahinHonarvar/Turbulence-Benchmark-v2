def filter_chars(s):
    chars_to_remove = set(s[18:82]) & set(range(ord('W'), ord('[') + 1))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))