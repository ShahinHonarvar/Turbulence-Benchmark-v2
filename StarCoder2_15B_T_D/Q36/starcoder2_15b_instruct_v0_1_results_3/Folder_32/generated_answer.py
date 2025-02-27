def filter_chars(s):
    return ''.join((c for c in s if c < '7' or c >= 'H' or c not in s[40:63]))