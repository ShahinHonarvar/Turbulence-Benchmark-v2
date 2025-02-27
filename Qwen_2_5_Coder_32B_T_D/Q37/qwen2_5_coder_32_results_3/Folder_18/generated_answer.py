def filter_chars(s):
    chars_to_remove = set(s[770:971]) & set('-ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join((c for c in s if c not in chars_to_remove))