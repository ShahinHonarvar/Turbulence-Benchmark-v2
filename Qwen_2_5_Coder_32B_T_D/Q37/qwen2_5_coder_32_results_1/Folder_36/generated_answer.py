def filter_chars(s):
    if len(s) < 503:
        return s
    chars_to_remove = set(s[259:503]) & set(range(ord(','), ord('4')))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))