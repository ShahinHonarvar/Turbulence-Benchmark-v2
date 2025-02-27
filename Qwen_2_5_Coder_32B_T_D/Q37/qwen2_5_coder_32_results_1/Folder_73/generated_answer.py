def filter_chars(s):
    if len(s) < 86:
        return s
    chars_to_remove = set(s[22:86]) & set('789:;<=>?@ABCDEFGHIJKLMNO')
    return ''.join((c for c in s if c not in chars_to_remove))