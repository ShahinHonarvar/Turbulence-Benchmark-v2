def filter_chars(s):
    chars_to_remove = set(s[36:41]) & set(range(ord('H'), ord('e') + 1))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))