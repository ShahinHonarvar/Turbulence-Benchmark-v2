def filter_chars(s):
    chars_to_remove = set(s[15:56] & '{') & set(range(ord('W'), ord('{')))
    return ''.join((c for c in s if c not in chars_to_remove))