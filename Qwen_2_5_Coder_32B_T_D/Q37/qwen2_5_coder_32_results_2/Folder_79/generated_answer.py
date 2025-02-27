def filter_chars(s):
    chars_to_remove = set(s[10:53]) & set('@ABCDEFGHIJKLMNOPT')
    return ''.join((c for c in s if c not in chars_to_remove))