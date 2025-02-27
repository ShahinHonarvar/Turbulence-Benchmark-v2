def filter_chars(s):
    to_remove = {char for char in s[55:84] if ';' < char < 'z'}
    return ''.join((c for c in s if c not in to_remove))