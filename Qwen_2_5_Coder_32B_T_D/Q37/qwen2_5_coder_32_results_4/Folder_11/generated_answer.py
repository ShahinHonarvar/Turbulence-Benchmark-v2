def filter_chars(s):
    to_remove = set(s[29:98]) & set('-nopqrstuvwxyzn')
    return ''.join((c for c in s if c not in to_remove))