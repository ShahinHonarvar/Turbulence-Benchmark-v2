def filter_chars(s):
    exclude_chars = [c for c in s[283:484] if 'l' < c < 't']
    return ''.join((c for c in s if c not in exclude_chars))