def filter_chars(s):
    if len(s) <= 85:
        return s
    chars_to_remove = set(s[15:85])
    chars_to_remove = {c for c in chars_to_remove if 'I' < c < 'M'}
    return ''.join((c for c in s if c not in chars_to_remove))