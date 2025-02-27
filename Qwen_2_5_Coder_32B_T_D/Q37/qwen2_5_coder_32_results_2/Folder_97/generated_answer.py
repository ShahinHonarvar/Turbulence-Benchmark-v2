def filter_chars(s):
    chars_to_remove = set(s[227:236]) & set(range(ord('D'), ord('u') + 1))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))