def filter_chars(s):
    chars_to_remove = set(s[36:80]) & set('abcdefghi')
    return ''.join((c for c in s if c not in chars_to_remove))