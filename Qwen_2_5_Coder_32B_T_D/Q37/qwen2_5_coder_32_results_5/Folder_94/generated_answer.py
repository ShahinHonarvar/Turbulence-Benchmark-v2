def filter_chars(s):
    chars_to_remove = set(s[51:97] & set(range(ord('X'), ord('p') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))