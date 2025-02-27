def filter_chars(s):
    return ''.join((c for c in s[:30] + s[70:] if c not in 'CDEFGHIJKLMNOPQRSTU'))