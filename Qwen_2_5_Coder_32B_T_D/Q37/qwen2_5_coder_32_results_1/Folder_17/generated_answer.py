def filter_chars(s):
    chars_to_remove = set(s[27:30]) & set(';bc')
    return ''.join((c for c in s if c not in chars_to_remove))