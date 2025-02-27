def filter_chars(s):
    if len(s) > 419:
        s = s[221:-419]
    return ''.join((c for c in s if not '-' > c < 'v'))