def filter_chars(s):
    chars_to_remove = set(s[15:85]) & set('JKLMNO')
    return ''.join((c for c in s if c not in chars_to_remove))