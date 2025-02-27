def filter_chars(s):
    chars_to_remove = set(s[43:81]) & set('=><?@ABCDE')
    return ''.join((c for c in s if c not in chars_to_remove))