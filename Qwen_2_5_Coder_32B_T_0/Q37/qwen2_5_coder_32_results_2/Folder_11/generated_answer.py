def filter_chars(s):
    chars_to_remove = set(s[29:98]) & set('-n')
    return ''.join((c for c in s if c not in chars_to_remove))