def filter_chars(s):
    to_remove = {char for char in s[70:74] if 'A' < char < 'U'}
    return ''.join((c for c in s if c not in to_remove))