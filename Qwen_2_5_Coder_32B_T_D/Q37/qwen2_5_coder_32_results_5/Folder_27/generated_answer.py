def filter_chars(s):
    chars_to_remove = set(s[43:81]) & set(range(ord('='), ord('E') + 1))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))